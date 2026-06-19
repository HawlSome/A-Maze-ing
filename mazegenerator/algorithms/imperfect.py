#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   imperfect.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 22:20:47 by varandri            #+#    #+#            #
#   Updated: 2026/06/20 00:24:47 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Directions, Maze
from ..functions import (
    connect_cells, get_corridor_walls
)
from typing import Callable
import random


def _update_5x5_corridors(
    grid: list[list[Cell]],
    all_corridors: dict[tuple[int, int], (list[int] | None)],
    curr_cell: tuple[int, int],
    next_cell: tuple[int, int]
) -> None:
    """Recalculate corridor wall counts in a 5x5 neighborhood around two cells.

    When a wall is removed between two adjacent cells, the corridor density
    for nearby cells changes. This function invalidates and recalculates the
    cached wall counts for all cells in a 5x5 neighborhood centered around
    both the current and next cells, ensuring the cache stays synchronized
    with actual grid state.

    Args:
        grid (list[list[Cell]]): The maze grid.
        all_corridors (dict): Corridor cache mapping (x, y) to wall counts.
            Updated in-place.
        curr_cell (tuple[int, int]): (x, y) position of the first cell
            involved in the wall removal.
        next_cell (tuple[int, int]): (x, y) position of the adjacent cell
            being connected to curr_cell.

    Note:
        The 5x5 neighborhood spans from offset -2 to +2 in both axes,
        providing a safety margin for corridor heuristics that examine
        neighboring wall densities.
    """
    w_grid: int = len(grid[0])
    h_grid: int = len(grid)

    for y in range(-2, 3):
        for x in range(-2, 3):
            curr_x, curr_y = curr_cell[0] + x, curr_cell[1] + y
            if (
                curr_x in range(w_grid) and
                curr_y in range(h_grid)
            ):
                all_corridors[(curr_x, curr_x)] = get_corridor_walls(
                    grid[curr_y][curr_y],
                    grid
                )

            next_x, next_y = next_cell[0] + x, next_cell[1] + y
            if (
                next_x in range(w_grid) and
                next_y in range(h_grid)
            ):
                all_corridors[next_x, next_y] = get_corridor_walls(
                    grid[next_y][next_x],
                    grid
                )


def imperfect_algorithm(
        algorithm: Callable,
        maze: Maze, rand: random.Random, imperfection: float | None = None
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Generate an imperfect maze using a pluggable carving algorithm.

    This function wraps any perfect maze carving algorithm and extends it
    by removing additional walls to introduce loops and cycles. The wrapped
    algorithm generates the initial perfect maze structure, then this
    function strategically breaks walls based on corridor density heuristics.

    Args:
        algorithm (Callable): A perfect maze carving function with signature
            (maze: Maze, rand: random.Random) -> list. Examples: dfs_perfect,
            prim_perfect, etc. The algorithm modifies the maze in-place.
        maze (Maze): Maze instance to modify in-place.
        rand (random.Random): Random generator used for selection and
            for determinism when seeded.
        imperfection (float | None): Fraction (0.0-1.0) of total walls
            to attempt to remove. If None, a random value from
            `rand.random()` is used.

    Returns:
        list[tuple[tuple[int,int], tuple[int,int]] | None]: The list of
        connection moves from the initial perfect maze carving, with
        additional wall removals applied as side effects on `maze`.
    """
    moves: list[
        (tuple[tuple[int, int], tuple[int, int]] | None)
    ] = algorithm(maze, rand)
    grid: list[list[Cell]] = maze.get_cells()
    total_walls: int = (len(grid) * len(grid[0]) * 4)
    if imperfection is None:
        imperfection = rand.random()
    walls_to_remove: int = int(total_walls * imperfection)
    max_attempts: int = walls_to_remove * 5

    if len(grid[0]) <= 3 or len(grid) <= 3:
        while walls_to_remove and max_attempts:
            x = rand.randint(0, len(grid[0]) - 1)
            y = rand.randint(0, len(grid) - 1)
            cell = grid[y][x]
            if cell.get_protect():
                continue
            max_attempts -= 1
            if (
                x + 1 in range(len(grid[0])) and
                cell.has_wall(Directions.E)
            ):
                cell.set_visit()
                grid[y][x + 1].set_visit()
                if (connect_cells(cell, grid[y][x + 1])) is not None:
                    walls_to_remove -= 1
            if (
                y + 1 in range(len(grid)) and
                cell.has_wall(Directions.S)
            ):
                cell.set_visit()
                grid[y + 1][x].set_visit()
                if (connect_cells(cell, grid[y + 1][x])) is not None:
                    walls_to_remove -= 1
        return moves

    all_corridor: dict[tuple[int, int], (list[int] | None)] = {
        (x, y): get_corridor_walls(grid[y][x], grid)
        for y in range(len(grid))
        for x in range(len(grid[0]))
    }

    if len(grid[0]) == 3 and len(grid) == 3:
        walls_removed_3x3: int = 0
        max_walls_3x3: int = 1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if walls_removed_3x3 >= max_walls_3x3:
                    return moves
                cell = grid[y][x]
                if (
                    cell.has_wall(Directions.E) and
                    (x + 1) in range(len(grid[0]))
                ):
                    walls_center: list[int] | None = all_corridor[(1, 1)]
                    if walls_center and min(walls_center) > 13:
                        cell.set_visit()
                        grid[y][x + 1].set_visit()
                        if connect_cells(cell, grid[y][x + 1]) is not None:
                            walls_removed_3x3 += 1
                            all_corridor[(1, 1)] = get_corridor_walls(
                                grid[1][1], grid
                            )
                            if walls_removed_3x3 >= max_walls_3x3:
                                return moves
                if (
                    cell.has_wall(Directions.S) and
                    (y + 1) in range(len(grid))
                ):
                    walls_center = all_corridor[(1, 1)]
                    if walls_center and min(walls_center) > 13:
                        cell.set_visit()
                        grid[y + 1][x].set_visit()
                        if connect_cells(cell, grid[y + 1][x]) is not None:
                            walls_removed_3x3 += 1
                            all_corridor[(1, 1)] = get_corridor_walls(
                                grid[1][1], grid
                            )
                            if walls_removed_3x3 >= max_walls_3x3:
                                return moves
        return moves

    while walls_to_remove and max_attempts:
        x = rand.randint(0, len(grid[0]) - 1)
        y = rand.randint(0, len(grid) - 1)
        cell = grid[y][x]
        if cell.get_protect():
            continue
        max_attempts -= 1
        if (
            x + 1 in range(len(grid[0])) and
            cell.has_wall(Directions.E)
        ):
            walls_neighbor_west: list[int] | None = all_corridor[(x + 1, y)]
            if walls_neighbor_west and min(walls_neighbor_west) > 13:
                cell.set_visit()
                grid[y][x + 1].set_visit()
                if (connect_cells(cell, grid[y][x + 1])) is not None:
                    walls_to_remove -= 1
                    _update_5x5_corridors(
                        grid,
                        all_corridor,
                        (x, y),
                        (x + 1, y)
                    )
        if (
            y + 1 in range(len(grid)) and
            cell.has_wall(Directions.S)
        ):
            walls_neighbor_south: list[int] | None = all_corridor[(x, y + 1)]
            if walls_neighbor_south and min(walls_neighbor_south) > 13:
                cell.set_visit()
                grid[y + 1][x].set_visit()
                if (connect_cells(cell, grid[y + 1][x])) is not None:
                    walls_to_remove -= 1
                    _update_5x5_corridors(
                        grid,
                        all_corridor,
                        (x, y),
                        (x, y + 1)
                    )
    return moves

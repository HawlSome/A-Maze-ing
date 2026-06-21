#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 17:24:37 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Maze, Directions
from ..functions import (
    get_neighbors, connect_cells, get_corridor_walls,
)
import random


def prims_perfect(
        maze: Maze, rand: random.Random
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Carve a perfect maze using Prim's algorithm (randomized variant).

    The function grows a spanning tree by repeatedly selecting a
    random edge that connects a visited cell to an unvisited cell and
    removing the wall between them, to produce a perfect maze.

    Args:
        maze (Maze): Maze instance to modify in-place.
        rand (random.Random): Random generator used for selection and
            for determinism when seeded.

    Returns:
        list[tuple[tuple[int,int], tuple[int,int]] | None]: A list of
        connection moves produced by `connect_cells`. Each element is
        typically a tuple of two cell coordinate tuples representing
        the connected cells, or None when no connection was made.
    """
    cells: list[list[Cell]] = maze.get_cells()
    edges: list[tuple[Cell, Cell]] = []
    moves: list[(tuple[tuple[int, int], tuple[int, int]] | None)] = []

    rand_y: int = rand.randint(0, len(cells) - 1)
    rand_x: int = rand.randint(0, len(cells[rand_y]) - 1)
    start: Cell = cells[rand_y][rand_x]
    start.set_visit()
    edges.extend(get_neighbors(start, cells))

    while len(edges):
        i: int = rand.randint(0, len(edges) - 1)
        current: tuple[Cell, Cell] = edges[i]
        edges[i] = edges[0]
        edges.pop(0)

        visited, unvisited = current
        connection: (
            tuple[tuple[int, int], tuple[int, int]] | None
        ) = connect_cells(visited, unvisited)
        if (connection):
            moves.append(connection)
            edges.extend(get_neighbors(unvisited, cells))
    return moves


def prims_imperfect(
        maze: Maze, rand: random.Random, imperfection: float | None = None
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Create an imperfect maze by first carving a perfect maze with
    Prim's algorithm, then removing additional walls to introduce loops.

    The function calls `prims_perfect` to produce an initial perfect
    maze, then remove additional walls according to the ``imperfection``
    fraction. Removal attempts avoid protected cells and use local
    corridor heuristics to breake long corridor walls.

    Args:
        maze (Maze): Maze instance to modify in-place.
        rand (random.Random): Random generator used for selection and
            for determinism when seeded.
        imperfection (float | None): Fraction (0.0-1.0) of total walls
            to attempt to remove. If None, a random value from
            `rand.random()` is used.

    Returns:
        list[tuple[tuple[int,int], tuple[int,int]] | None]: The list of
        moves returned by the initial `prims_perfect` carving. Additional
        wall removals are applied as side effects on `maze`.
    """
    moves: list[
        (tuple[tuple[int, int], tuple[int, int]] | None)
    ] = prims_perfect(maze, rand)
    grid: list[list[Cell]] = maze.get_cells()
    all_corridor: dict[tuple[int, int], (list[int] | None)] = {
        (x, y): get_corridor_walls(grid[y][x], grid)
        for y in range(len(grid))
        for x in range(len(grid[0]))
    }
    total_walls: int = (len(grid) * len(grid[0]) * 4)
    if imperfection is None:
        imperfection = rand.random()
    walls_to_remove: int = int(total_walls * imperfection)
    max_attempts: int = walls_to_remove * 5
    while walls_to_remove and max_attempts:
        x: int = rand.randint(0, len(grid[0]) - 1)
        y: int = rand.randint(0, len(grid) - 1)
        cell: Cell = grid[y][x]
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
                    for delim_y in range(-2, 3):
                        for delim_x in range(-2, 3):
                            curr_x, curr_y = (x + delim_x, y + delim_y)
                            curr_x_1, curr_y_1 = (
                                (x + 1) + delim_x, y + delim_y
                            )
                            if (
                                curr_x in range(len(grid[0])) and
                                curr_y in range(len(grid))
                            ):
                                all_corridor[(curr_x, curr_y)] = (
                                    get_corridor_walls(
                                        grid[curr_y][curr_x], grid
                                    )
                                )
                            if (
                                curr_x_1 in range(len(grid[0])) and
                                curr_y_1 in range(len(grid))
                            ):
                                all_corridor[(curr_x_1, curr_y_1)] = (
                                    get_corridor_walls(
                                        grid[curr_y_1][curr_x_1], grid
                                    )
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
                    for delim_y in range(-2, 3):
                        for delim_x in range(-2, 3):
                            curr_x, curr_y = (x + delim_x, y + delim_y)
                            curr_x_1, curr_y_1 = (
                                x + delim_x, (y + 1) + delim_y
                            )
                            if (
                                curr_x in range(len(grid[0])) and
                                curr_y in range(len(grid))
                            ):
                                all_corridor[(curr_x, curr_y)] = (
                                    get_corridor_walls(
                                        grid[curr_y][curr_x], grid
                                    )
                                )
                            if (
                                curr_x_1 in range(len(grid[0])) and
                                curr_y_1 in range(len(grid))
                            ):
                                all_corridor[(curr_x_1, curr_y_1)] = (
                                    get_corridor_walls(
                                        grid[curr_y_1][curr_x_1], grid
                                    )
                                )
    return moves


def prims_carver(
        maze: Maze, seed: int | None, perfect: bool | None = True
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Entry point to carve a maze using prims-based algorithms.

    It's a wrapper that creates a `random.Random` instance using
    the provided ``seed`` (if any) and dispatches to either
    `prims_perfect` or `prims_imperfect` depending on ``perfect``.

    Args:
        maze (Maze): Maze instance to modify in-place.
        seed (int | None): Optional integer seed for reproducible
            randomness. If None, an unseeded generator is used.
        perfect (bool | None): If True (default) create a perfect
            maze; otherwise create an imperfect maze with loops.

    Returns:
        list[tuple[tuple[int,int], tuple[int,int]] | None]: The list of
        connection moves produced by the chosen algorithm.
    """
    rand: random.Random = random.Random()
    if seed:
        rand = random.Random(seed)
    if perfect:
        return prims_perfect(maze, rand)
    else:
        return prims_imperfect(maze, rand)

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   dfs.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 19:14:38 by nrasolom            #+#    #+#            #
#   Updated: 2026/06/06 07:36:33 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Directions, Maze
from ..functions import (
    get_neighbors, connect_cells, get_corridor_walls
)
import random


def dfs_perfect(
        maze: Maze, rand: random.Random
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:

    moves: list[(tuple[tuple[int, int], tuple[int, int]] | None)] = []

    grid = maze.get_cells()
    x = rand.randint(0, len(grid[0]) - 1)
    y = rand.randint(0, len(grid) - 1)

    start_cell = grid[y][x]
    while start_cell.get_protect() is True:
        x = rand.randint(0, len(grid[0]) - 1)
        y = rand.randint(0, len(grid) - 1)
        start_cell = grid[y][x]

    stack = [start_cell]
    start_cell.set_visit()

    while stack:
        actual_cell = stack[-1]
        neighbors = get_neighbors(actual_cell, grid)

        if neighbors:
            neighbor_cell = rand.choice(neighbors)[1]
            connected = connect_cells(actual_cell, neighbor_cell, True)
            if connected:
                moves.append(connected)
            stack.append(neighbor_cell)
        else:
            stack.pop()
    return moves


def dfs_imperfect(
        maze: Maze, rand: random.Random, imperfection: float | None = None
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    moves: list[
        (tuple[tuple[int, int], tuple[int, int]] | None)
    ] = dfs_perfect(maze, rand)
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
        print("\r loading ...", end="")
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


def dfs_carver(
        maze: Maze, seed: int | None, perfect: bool | None = True
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    rand: random.Random = random.Random()
    if seed:
        rand = random.Random(seed)
    if perfect:
        return dfs_perfect(maze, rand)
    else:
        return dfs_imperfect(maze, rand)

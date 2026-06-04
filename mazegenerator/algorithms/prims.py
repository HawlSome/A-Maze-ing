#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/04 16:14:50 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Maze, Directions
from ..functions import (
    get_neighbors, connect_cells, get_corridors, get_corridor_walls,
    get_corridors_tuple, get_corridors_bounds
)
import random


def prims_perfect(
        maze: Maze, rand: random.Random
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
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
    moves: list[
        (tuple[tuple[int, int], tuple[int, int]] | None)
    ] = prims_perfect(maze, rand)
    grid: list[list[Cell]] = maze.get_cells()
    total_walls: int = (len(grid) * len(grid[0]) * 4)
    if imperfection is None:
        imperfection = rand.random()
    walls_to_remove: int = int(total_walls * imperfection)
    for _ in range(len(grid)):
        if not walls_to_remove:
            break
        for _ in range(len(grid[0])):
            if not walls_to_remove:
                break
            x: int = rand.randint(0, len(grid[0]) - 1)
            y: int = rand.randint(0, len(grid) - 1)
            cell: Cell = grid[y][x]
            if cell.get_protect():
                continue
            corridors: list[list[Cell]] = get_corridors(cell, grid)
            corridors_bounds: list[
                list[tuple[int, int]]
            ] = get_corridors_bounds(
                    get_corridors_tuple(corridors)
            )
            walls: list[int] | None = get_corridor_walls(corridors, grid)
            if walls:
                corridors_walls: list[
                    tuple[list[Cell], int, list[tuple[int, int]]]
                ] = [
                    (corridor, wall, bounds)
                    for (corridor, wall, bounds) in zip(
                        corridors, walls, corridors_bounds
                    )
                    if wall > 9
                ]
                if corridors_walls:
                    corridor, _, bounds = rand.choice(corridors_walls)
                    cell = rand.choice(corridor)
                    (x_min, x_max), (y_min, y_max) = bounds
                    x, y = cell.get_coordinate()
                    if (
                        x in range(x_min, x_max) and
                        cell.has_wall(Directions.E)
                    ):
                        cell.set_visit()
                        grid[y][x + 1].set_visit()
                        if (connect_cells(cell, grid[y][x + 1])) is not None:
                            walls_to_remove -= 1
                    if (
                        y in range(y_min, y_max) and
                        cell.has_wall(Directions.S)
                    ):
                        cell.set_visit()
                        grid[y + 1][x].set_visit()
                        if (connect_cells(cell, grid[y][x])) is not None:
                            walls_to_remove -= 1
    return moves


def prims_carver(
        maze: Maze, seed: int | None, perfect: bool | None = True
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    rand: random.Random = random.Random()
    if seed:
        rand = random.Random(seed)
    if perfect:
        return prims_perfect(maze, rand)
    else:
        return prims_imperfect(maze, rand)

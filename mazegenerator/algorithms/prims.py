#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/05 12:36:18 by varandri           ###   ########.fr      #
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
    max_attempts: int = walls_to_remove * 2
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
            walls_neighbor_west: list[int] | None = get_corridor_walls(
                grid[y][x + 1], grid
            )
            if walls_neighbor_west and min(walls_neighbor_west) > 13:
                cell.set_visit()
                grid[y][x + 1].set_visit()
                if (connect_cells(cell, grid[y][x + 1])) is not None:
                    walls_to_remove -= 1
        if (
            y + 1 in range(len(grid)) and
            cell.has_wall(Directions.S)
        ):
            walls_neighbor_south: list[int] | None = get_corridor_walls(
                grid[y + 1][x], grid
            )
            if walls_neighbor_south and min(walls_neighbor_south) > 13:
                cell.set_visit()
                cell.set_visit()
                grid[y + 1][x].set_visit()
                if (connect_cells(cell, grid[y + 1][x])) is not None:
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

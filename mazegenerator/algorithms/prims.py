#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 23:05:32 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Maze
from ..functions import get_neighbors, connect_cells
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
        maze: Maze, rand: random.Random
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    moves: list[
        (tuple[tuple[int, int], tuple[int, int]] | None)
    ] = prims_perfect(maze, rand)

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
        return prims_perfect(maze, rand)

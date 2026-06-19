#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/20 00:27:30 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Maze
from ..functions import (
    get_neighbors, connect_cells
)
from .imperfect import imperfect_algorithm
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
        return imperfect_algorithm(prims_perfect, maze, rand)

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dfs.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 19:14:38 by nrasolom            #+#    #+#            #
#   Updated: 2026/06/19 22:32:12 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Maze
from ..functions import (
    get_neighbors, connect_cells
)
from .imperfect import imperfect_algorithm
import random


def dfs_perfect(
        maze: Maze, rand: random.Random
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Carve a perfect maze using depth-first search (recursive backtracker).

    The function performs an iterative DFS starting from a random,
    unprotected cell. It connects cells by removing walls until all
    reachable cells have been visited, producing a perfect maze.

    Args:
        maze (Maze): Maze instance to modify in-place
        rand (random.Random): Random generator used for selection and
            for determinism when seeded.

    Returns:
        list[tuple[tuple[int,int], tuple[int,int]] | None]: A list of
        connection moves produced by `connect_cells`. Each element is
        typically a tuple of two cell coordinate tuples representing
        the connected cells, or None when no connection was made.
    """
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
            connected = connect_cells(actual_cell, neighbor_cell)
            if connected:
                moves.append(connected)
            stack.append(neighbor_cell)
        else:
            stack.pop()
    return moves


def dfs_carver(
        maze: Maze, seed: int | None, perfect: bool | None = True
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Entry point to carve a maze using DFS-based algorithms.

    It's a wrapper that creates a `random.Random` instance using
    the provided ``seed`` (if any) and dispatches to either
    `dfs_perfect` or `dfs_imperfect` depending on ``perfect``.

    Args:
        maze (Maze): Maze instance to modify in-place
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
        return dfs_perfect(maze, rand)
    else:
        return imperfect_algorithm(dfs_perfect, maze, rand)

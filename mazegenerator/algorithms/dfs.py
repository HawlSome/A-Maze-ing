#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dfs.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 19:14:38 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/17 11:02:39 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Directions, Maze
from ..utils import get_neighbors, connect_cells
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
        maze: Maze, rand: random.Random, imperfection: float = 0.2
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:

    moves = dfs_perfect(maze, rand)

    remaining_walls: list[tuple[Cell, Cell]] = []
    grid = maze.get_cells()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell.get_protect() is True:
                continue

            if x < len(grid[0]) - 1:
                if cell.has_wall(Directions.E):
                    remaining_walls.append((cell, grid[y][x + 1]))

            if y < len(grid) - 1:
                if cell.has_wall(Directions.S):
                    remaining_walls.append((cell, grid[y + 1][x]))

    walls_to_remove = int(len(remaining_walls) * imperfection)
    selected_walls = rand.sample(remaining_walls, walls_to_remove)
    for actual_cell, neighbor in selected_walls:
        actual_cell.unset_visit()
        neighbor.unset_visit()
        connected = connect_cells(actual_cell, neighbor)
        if connected:
            moves.append(connected)

    return moves


def dfs(
        maze: Maze, seed: int | None, perfect: bool | None = True
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    rand: random.Random = random.Random()
    if seed:
        rand = random.Random(seed)
    if perfect:
        return dfs_perfect(maze, rand)
    else:
        return dfs_imperfect(maze, rand)

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dfs.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 19:14:38 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/03 15:49:09 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell, Directions
from utils.utils_cells import get_neighbors, connect_cells
import random


def dfs(start_cell: "Cell", grid: list[list[Cell]]):
    stack = [start_cell]
    start_cell.set_visit

    while stack:
        actual_cell = stack[-1]
        univisited_neighbors = [cell
                                for cell in get_neighbors(actual_cell, grid)
                                if not cell.get_visit()]

        if univisited_neighbors:
            neighbor_cell = random.choice(univisited_neighbors)
            connect_cells(actual_cell, neighbor_cell)
            neighbor_cell.set_visit
            stack.append(neighbor_cell)
        else:
            stack.pop()


def gen_perfect_maze(grid: list[list[Cell]]) -> list[list[Cell]]:
    x = random.randint(0, len(grid[0]) - 1)
    y = random.randint(0, len(grid) - 1)

    start_cell = grid[y][x]
    dfs(start_cell, grid)
    return grid


def gen_imperfect_maze(grid: list[list[Cell]],
                       imperfection: float) -> list[list[Cell]]:
    gen_perfect_maze(grid)

    remaining_walls: list[tuple[Cell, Cell]] = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]

            if x < len(grid[0]) - 1:
                if cell.has_wall(Directions.E):
                    remaining_walls.append((cell, grid[y][x + 1]))

            if y < len(grid) - 1:
                if cell.has_wall(Directions.S):
                    remaining_walls.append((cell, grid[y + 1][x]))

    walls_to_remove = int(len(remaining_walls) * imperfection)
    selected_walls = random.sample(remaining_walls, walls_to_remove)
    for actual_cell, neighbor in selected_walls:
        connect_cells(actual_cell, neighbor)

    return grid

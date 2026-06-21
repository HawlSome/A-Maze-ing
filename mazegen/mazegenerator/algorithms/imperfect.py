#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   imperfect.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 22:20:47 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 12:20:26 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Directions, Maze
from ..functions import connect_cells
from typing import Callable
import random


def _can_remove_wall(
        grid: list[list[Cell]], x: int, y: int, direction: Directions
) -> bool:
    """Check if removing a wall creates a fully open 3x3 corridor.

    Scans ALL possible 3x3 regions in the maze. If the wall removal would
    leave any 3x3 region with 0 internal walls, returns False.
    """
    h, w = len(grid), len(grid[0])
    x2, y2 = (x + 1, y) if direction == Directions.E else (x, y + 1)

    for start_y in range(max(0, h - 2)):
        for start_x in range(max(0, w - 2)):
            region_has_wall = False
            for dy in range(3):
                for dx in range(3):
                    if (start_y + dy, start_x + dx) in [(y, x), (y2, x2)]:
                        region_has_wall = True
                        break
            if not region_has_wall:
                continue
            wall_count = 0
            for dy in range(3):
                for dx in range(2):
                    cell = grid[start_y + dy][start_x + dx]
                    if cell.has_wall(Directions.E):
                        wall_count += 1

            for dy in range(2):
                for dx in range(3):
                    cell = grid[start_y + dy][start_x + dx]
                    if cell.has_wall(Directions.S):
                        wall_count += 1

            if wall_count <= 1:
                return False

    return True


def imperfect_algorithm(
     algorithm: Callable[[Maze, random.Random], list[
            tuple[tuple[int, int], tuple[int, int]] | None
         ]],
     maze: Maze, rand: random.Random, imperfection: float | None = None
) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
    """Generate an imperfect maze by removing walls from a perfect maze.

    Removes walls randomly to create loops, while preventing any 3x3
    region from becoming completely open.

    Args:
    algorithm (Callable): Perfect maze carving function.
    maze (Maze): Maze instance to modify in-place.
    rand (random.Random): Random generator.
    imperfection (float | None): Fraction of walls to attempt removing.

    Returns:
    list: Connection moves from the initial perfect maze carving.
    """
    moves = algorithm(maze, rand)
    grid = maze.get_cells()

    if imperfection is None or 1 < imperfection < 0:
        imperfection = rand.randint(0, 1)

    total_walls = len(grid) * len(grid[0]) * 4
    walls_to_remove = int(total_walls * imperfection)
    while walls_to_remove == 0:
        imperfection = rand.randint(0, 1)
        walls_to_remove = int(total_walls * imperfection)
    removed_walls = 0
    attempts = 0
    max_attempts = walls_to_remove * 5

    while walls_to_remove and attempts < max_attempts:
        attempts += 1
        x = rand.randint(0, len(grid[0]) - 1)
        y = rand.randint(0, len(grid) - 1)
        cell = grid[y][x]

        if cell.get_protect():
            continue

        if x + 1 < len(grid[0]) and cell.has_wall(Directions.E):
            if _can_remove_wall(grid, x, y, Directions.E):
                cell.set_visit()
                grid[y][x + 1].set_visit()
                connect_cells(cell, grid[y][x + 1])
                removed_walls += 1
                walls_to_remove -= 1
                continue

        if y + 1 < len(grid) and cell.has_wall(Directions.S):
            if _can_remove_wall(grid, x, y, Directions.S):
                cell.set_visit()
                grid[y + 1][x].set_visit()
                connect_cells(cell, grid[y + 1][x])
                removed_walls += 1
                walls_to_remove -= 1

    return moves

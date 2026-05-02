#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cells_utils.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 13:27:44 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 19:24:01 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell, Wall


def generate_cells(width: int, height: int) -> list[list["Cell"]]:
    return [[Cell(i, j) for i in range(width)] for j in range(height)]


def remove_wall_between(cell_a: "Cell", cell_b: "Cell",
                        direction: "Wall") -> None:
    cell_a.open_wall(direction)
    cell_b.open_wall(direction.opposite())


def get_neighbors(current: Cell, grid: list[list[Cell]]) -> list[Cell]:
    neighbors: list[Cell] = []
    width = len(grid[0]) - 1
    height = len(grid) - 1
    x, y = current.coordinate

    if x > 0:
        neighbors.append(grid[y][x - 1])
    if x < width:
        neighbors.append(grid[y][x + 1])
    if y > 0:
        neighbors.append(grid[y - 1][x])
    if y < height:
        neighbors.append(grid[y + 1][x])
    return neighbors


def connect_cells(cell_a: "Cell", cell_b: "Cell") -> None:
    a_x, a_y = cell_a.coordinate
    b_x, b_y = cell_b.coordinate

    if (a_x < b_x):
        remove_wall_between(cell_a, cell_b, Wall.EAST)
    elif (a_x > b_x):
        remove_wall_between(cell_a, cell_b, Wall.WEST)
    elif (a_y < b_y):
        remove_wall_between(cell_a, cell_b, Wall.SOUTH)
    elif (a_y > b_y):
        remove_wall_between(cell_a, cell_b, Wall.NORTH)

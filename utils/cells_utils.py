#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cells_utils.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 13:27:44 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 17:07:25 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell, Wall


def generate_cells(width: int, height: int) -> list[list["Cell"]]:
    return [[Cell(i,j) for i in range(width)] for j in range(height)]


def remove_wall_between(cell_a: "Cell", cell_b: "Cell",
                        direction: "Wall") -> None:
    cell_a.open_wall(direction)
    cell_b.open_wall(direction.opposite())


def get_neighbors(current: Cell, cells: list[list[Cell]]) -> list[Cell]:
    neighbors: list[Cell] = []
    width: int = len(cells[0]) - 1
    height: int = len(cells) - 1
    x, y = current.get_coordinate()

    if x > 0:
        neighbors.append(cells[y][x - 1])
    if x < width:
        neighbors.append(cells[y][x + 1])
    if y > 0:
        neighbors.append(cells[y - 1][x])
    if y < height:
        neighbors.append(cells[y + 1][x])
    return neighbors


def connect_cells(a: Cell, b: Cell) -> None:
    a_x, a_y = a.get_coordinate()
    b_x, b_y = b.get_coordinate()

    if (a_x < b_x):
        remove_wall_between(a, b, Wall.EAST)
    elif (a_x > b_x):
        remove_wall_between(a, b, Wall.WEST)
    elif (a_y < b_y):
        remove_wall_between(a, b, Wall.SOUTH)
    elif (a_y > b_y):
        remove_wall_between(a, b, Wall.NORTH)

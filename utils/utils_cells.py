# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   create_cells.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:09 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 17:13:47 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes import Cell
from .utils_cells_walls import open_west, open_east, open_north, open_south


def generate_cells(x: int, y: int) -> list[list[Cell]]:
    return [[Cell(i, j) for i in range(x)] for j in range(y)]
    # cells: list[list[Cell]] = []
    # for j in range(y):
    #     row: list[Cell] = []
    #     for i in range(x):
    #         row.append(Cell(i, j))
    #     cells.append(row)
    # return cells


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
        open_east(a, b)
    elif (a_x > b_x):
        open_west(a, b)
    elif (a_y < b_y):
        open_south(a, b)
    elif (a_y > b_y):
        open_north(a, b)
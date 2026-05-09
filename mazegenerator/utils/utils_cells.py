# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   utils_cells.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:09 by varandri            #+#    #+#            #
#   Updated: 2026/05/05 17:34:24 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell
from .utils_cells_walls import (
    open_west, open_east, open_north, open_south,
    close_west, close_east, close_north, close_south
)


def generate_cells(
        w: int, h: int, algorithm: str = "prims"
) -> list[list[Cell]]:
    return [[Cell(x, y) for x in range(w)] for y in range(h)]
    # cells: list[list[Cell]] = []
    # for j in range(y):
    #     row: list[Cell] = []
    #     for i in range(x):
    #         row.append(Cell(i, j))
    #     cells.append(row)
    # return cells


def get_neighbors(
        current: Cell, cells: list[list[Cell]]
) -> list[tuple[Cell, Cell]]:
    neighbors: list[tuple[Cell, Cell]] = []
    width: int = len(cells[0]) - 1
    height: int = len(cells) - 1
    x, y = current.get_coordinate()

    if x > 0 and (
        not cells[y][x - 1].get_protect() and
        not cells[y][x - 1].get_visit()
    ):
        neighbors.append((current, cells[y][x - 1]))
    if x < width and (
        not cells[y][x + 1].get_protect() and
        not cells[y][x + 1].get_visit()
    ):
        neighbors.append((current, cells[y][x + 1]))
    if y > 0 and (
        not cells[y - 1][x].get_protect() and
        not cells[y - 1][x].get_visit()
    ):
        neighbors.append((current, cells[y - 1][x]))
    if y < height and (
        not cells[y + 1][x].get_protect() and
        not cells[y + 1][x].get_visit()
    ):
        neighbors.append((current, cells[y + 1][x]))
    return neighbors


def connect_cells(
        a: Cell, b: Cell
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    if b.get_visit() or b.get_protect():
        return None
    a_x: int
    b_x: int
    a_y: int
    b_y: int
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
    b.set_visit()

    return ((a_x, a_y), (b_x, b_y))


def deconnect_cells(
        a: Cell, b: Cell
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    if a.get_next() is not b:
        return None
    a_x: int
    b_x: int
    a_y: int
    b_y: int
    a_x, a_y = a.get_coordinate()
    b_x, b_y = b.get_coordinate()

    if (a_x < b_x):
        close_east(a, b)
    elif (a_x > b_x):
        close_west(a, b)
    elif (a_y < b_y):
        close_south(a, b)
    elif (a_y > b_y):
        close_north(a, b)

    return ((a_x, a_y), (b_x, b_y))


# def define_nexts(cells: list[list[OriginCell]]) -> None:
#     x_max: int = len(cells[0])
#     y_max: int = len(cells)

#     for y in range(y_max):
#         for x in range(x_max):

#             if cells[y][x].get_visit():
#                 continue

#             if x < x_max - 1:
#                 next_x: int = x + 1
#                 # while next_x < x_max - 1 and cells[y][next_x].get_visit():
#                 #     next_x += 1
#                 # if not cells[y][next_x].get_visit():
#                 cells[y][x].set_next(cells[y][next_x])

#             if y < y_max - 1:
#                 next_y: int = y + 1
#                 # while next_y < y_max - 1 and cells[next_y][x].get_visit():
#                 #     next_y += 1
#                 # if not cells[y][next_y].get_visit():
#                 cells[y][x].set_next(cells[next_y][x])

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   cells_functions.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 13:03:12 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes.cell import Cell
from ..classes.directions import Directions
from .walls_functions import (
    open_west, open_east, open_north, open_south,
    close_west, close_east, close_north, close_south
)


def generate_cells(
        w: int, h: int
) -> list[list[Cell]]:
    """Create a 2D grid of `Cell` objects.

    Args:
        w (int): Width of the grid (number of columns).
        h (int): Height of the grid (number of rows).

    Returns:
        list[list[Cell]]: A list of rows, each a list of `Cell`.
    """
    return [[Cell(x, y) for x in range(w)] for y in range(h)]


def get_neighbors(
        current: Cell, cells: list[list[Cell]]
) -> list[tuple[Cell, Cell]]:
    """Return unvisited, unprotected neighbor cell pairs of a given cell.

    The returned list contains tuples of (current_cell, neighbor_cell)
    for each adjacent cell that is not protected and not yet visited.
    """
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


def get_accessible_neighbors(
        current: Cell, cells: list[list[Cell]]
) -> list[Cell]:
    """Return adjacent cells accessible from the current cell.

    Accessibility is determined by the absence of a wall between the
    current cell and the neighbor. Protected neighbors are filtered out.
    """
    neighbors: list[Cell] = []
    width: int = len(cells[0]) - 1
    height: int = len(cells) - 1
    x, y = current.get_coordinate()

    if x > 0 and not current.has_wall(Directions.W):
        neighbors.append(cells[y][x - 1])
    if x < width and not current.has_wall(Directions.E):
        neighbors.append(cells[y][x + 1])
    if y > 0 and not current.has_wall(Directions.N):
        neighbors.append(cells[y - 1][x])
    if y < height and not current.has_wall(Directions.S):
        neighbors.append(cells[y + 1][x])

    for neighbor in neighbors:
        if neighbor.get_protect():
            neighbors.remove(neighbor)

    return neighbors


def connect_cells(
        a: Cell, b: Cell
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Connect two adjacent cells by opening the shared wall.

    The function validates that the target cell is not visited or
    protected before opening the wall between `a` and `b` and marking
    the target as visited.

    Args:
        a (Cell): Origin cell.
        b (Cell): Destination cell.

    Returns:
        tuple[tuple[int,int], tuple[int,int]] | None: Coordinates of
        the connected cells, or None if connection was not allowed.
    """
    if b.get_visit() or b.get_protect() or a.get_protect():
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
    """Disconnect two adjacent cells by closing their shared wall.

    Args:
        a (Cell): Origin cell.
        b (Cell): Destination cell.

    Returns:
        tuple[tuple[int,int], tuple[int,int]] | None: Coordinates of the
        disconnected cells, or None if operation not applicable.
    """
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

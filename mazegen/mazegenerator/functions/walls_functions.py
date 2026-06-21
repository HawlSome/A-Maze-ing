#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   walls_functions.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:37:02 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 14:29:24 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ..classes.cell import Cell
from ..classes.directions import Directions


def open_west(a: Cell, b: Cell) -> None:
    """Open the west wall of `a` and the corresponding east wall of `b`.

    Args:
        a (Cell): The cell to be opened.
        b (Cell): The cell next to the cell to be opened.
    """
    a.open_wall(Directions.W)
    b.open_wall(Directions.W.opposite())


def open_south(a: Cell, b: Cell) -> None:
    """Open the south wall of `a` and the corresponding north wall of `b`.

    Args:
        a (Cell): The cell to be opened.
        b (Cell): The cell next to the cell to be opened.
    """
    a.open_wall(Directions.S)
    b.open_wall(Directions.S.opposite())


def open_east(a: Cell, b: Cell) -> None:
    """Open the east wall of `a` and the corresponding west wall of `b`.

    Args:
        a (Cell): The cell to be opened.
        b (Cell): The cell next to the cell to be opened.
    """
    a.open_wall(Directions.E)
    b.open_wall(Directions.E.opposite())


def open_north(a: Cell, b: Cell) -> None:
    """Open the north wall of `a` and the corresponding south wall of `b`.

    Args:
        a (Cell): The cell to be opened.
        b (Cell): The cell next to the cell to be opened.
    """
    a.open_wall(Directions.N)
    b.open_wall(Directions.N.opposite())


def close_west(a: Cell, b: Cell) -> None:
    """Close the wall between two horizontally adjacent cells (west).

    Args:
        a (Cell): The cell to be closed.
        b (Cell): The cell next to the cell to be closed.
    """
    a.close_wall(Directions.W)
    b.close_wall(Directions.W.opposite())


def close_south(a: Cell, b: Cell) -> None:
    """Close the wall between two vertically adjacent cells (south).

    Args:
        a (Cell): The cell to be closed.
        b (Cell): The cell next to the cell to be closed.
    """
    a.close_wall(Directions.S)
    b.close_wall(Directions.S.opposite())


def close_east(a: Cell, b: Cell) -> None:
    """Close the wall between two horizontally adjacent cells (east).

    Args:
        a (Cell): The cell to be closed.
        b (Cell): The cell next to the cell to be closed.
    """
    a.close_wall(Directions.E)
    b.close_wall(Directions.E.opposite())


def close_north(a: Cell, b: Cell) -> None:
    """Close the wall between two vertically adjacent cells (north).

    Args:
        a (Cell): The cell to be closed.
        b (Cell): The cell next to the cell to be closed.
    """
    a.close_wall(Directions.N)
    b.close_wall(Directions.N.opposite())

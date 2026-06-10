#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   walls_functions.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:37:02 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 13:08:04 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ..classes.cell import Cell
from ..classes.directions import Directions


def open_west(a: Cell, b: Cell) -> None:
    """Open the west wall of `a` and the corresponding east wall of `b`.

    Args:
        a (Cell): The cell on the east side that will have its west wall opened.
        b (Cell): The cell on the west side that will have its east wall opened.
    """
    a.open_wall(Directions.W)
    b.open_wall(Directions.W.opposite())


def open_south(a: Cell, b: Cell) -> None:
    """Open the south wall of `a` and the corresponding north wall of `b`."""
    a.open_wall(Directions.S)
    b.open_wall(Directions.S.opposite())


def open_east(a: Cell, b: Cell) -> None:
    """Open the east wall of `a` and the corresponding west wall of `b`."""
    a.open_wall(Directions.E)
    b.open_wall(Directions.E.opposite())


def open_north(a: Cell, b: Cell) -> None:
    """Open the north wall of `a` and the corresponding south wall of `b`."""
    a.open_wall(Directions.N)
    b.open_wall(Directions.N.opposite())


def close_west(a: Cell, b: Cell) -> None:
    """Close the wall between two horizontally adjacent cells (west)."""
    a.close_wall(Directions.W)
    b.close_wall(Directions.W.opposite())


def close_south(a: Cell, b: Cell) -> None:
    """Close the wall between two vertically adjacent cells (south)."""
    a.close_wall(Directions.S)
    b.close_wall(Directions.S.opposite())


def close_east(a: Cell, b: Cell) -> None:
    """Close the wall between two horizontally adjacent cells (east)."""
    a.close_wall(Directions.E)
    b.close_wall(Directions.E.opposite())


def close_north(a: Cell, b: Cell) -> None:
    """Close the wall between two vertically adjacent cells (north)."""
    a.close_wall(Directions.N)
    b.close_wall(Directions.N.opposite())

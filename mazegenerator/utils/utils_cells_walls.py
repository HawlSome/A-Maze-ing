# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   utils_cells_walls.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:37:02 by varandri            #+#    #+#            #
#   Updated: 2026/05/05 16:23:23 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from ..classes import Cell, Directions


def open_west(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.W)
    b.open_wall(Directions.W.opposite())


def open_south(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.S)
    b.open_wall(Directions.S.opposite())


def open_east(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.E)
    b.open_wall(Directions.E.opposite())


def open_north(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.N)
    b.open_wall(Directions.N.opposite())


def close_west(a: Cell, b: Cell) -> None:
    a.close_wall(Directions.W)
    b.close_wall(Directions.W.opposite())


def close_south(a: Cell, b: Cell) -> None:
    a.close_wall(Directions.S)
    b.close_wall(Directions.S.opposite())


def close_east(a: Cell, b: Cell) -> None:
    a.close_wall(Directions.E)
    b.close_wall(Directions.E.opposite())


def close_north(a: Cell, b: Cell) -> None:
    a.close_wall(Directions.N)
    b.close_wall(Directions.N.opposite())

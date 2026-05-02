# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   utils_cells_walls.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:37:02 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 11:10:11 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from classes import Cell, Directions


def open_west(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.WEST)
    b.open_wall(Directions.WEST.opposite())


def open_south(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.SOUTH)
    b.open_wall(Directions.SOUTH.opposite())


def open_east(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.EAST)
    b.open_wall(Directions.EAST.opposite())


def open_north(a: Cell, b: Cell) -> None:
    a.open_wall(Directions.NORTH)
    b.open_wall(Directions.NORTH.opposite())

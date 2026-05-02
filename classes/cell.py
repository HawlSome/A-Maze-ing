# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 11:56:14 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .directions import Directions


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self._coordinate: tuple[int, int] = (x, y)
        self._north: int = 1
        self._south: int = 1
        self._west: int = 1
        self._east: int = 1
        self._isolation: bool = False

    def get_coordinate(self) -> tuple[int, int]:
        return self._coordinate

    def open_wall(self, wall: Directions) -> None:
        if self._isolation:
            return
        if wall == Directions.WEST:
            self._west = 0
        elif wall == Directions.SOUTH:
            self._south = 0
        elif wall == Directions.EAST:
            self._east = 0
        elif wall == Directions.NORTH:
            self._north = 0
        else:
            return

    def close_wall(self, wall: Directions) -> None:
        if self._isolation:
            return
        if wall == Directions.WEST:
            self._west = 1
        elif wall == Directions.SOUTH:
            self._south = 1
        elif wall == Directions.EAST:
            self._east = 1
        elif wall == Directions.NORTH:
            self._north = 1
        else:
            return

    def set_isolation(self) -> None:
        self._isolation = True

    def get_hex(self) -> str:
        bits: list[int] = [self._west, self._south, self._east, self._north]
        int_value: int = int("".join(map(str, bits)), 2)
        hex_value: str = hex(int_value)
        return hex_value[2:]

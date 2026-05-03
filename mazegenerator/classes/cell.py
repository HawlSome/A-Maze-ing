#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/03 15:47:15 by nrasolom           ###   ########.fr      #
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
        self._visited: bool = False

    def get_coordinate(self) -> tuple[int, int]:
        return self._coordinate

    def has_wall(self, wall: Directions) -> int:
        if wall == Directions.W:
            return self._west
        elif wall == Directions.S:
            return self._south
        elif wall == Directions.E:
            return self._east
        elif wall == Directions.N:
            return self._north
        else:
            return

    def open_wall(self, wall: Directions) -> None:
        if self._visited:
            return
        if wall == Directions.W:
            self._west = 0
        elif wall == Directions.S:
            self._south = 0
        elif wall == Directions.E:
            self._east = 0
        elif wall == Directions.N:
            self._north = 0
        else:
            return

    def close_wall(self, wall: Directions) -> None:
        if self._visited:
            return
        if wall == Directions.W:
            self._west = 1
        elif wall == Directions.S:
            self._south = 1
        elif wall == Directions.E:
            self._east = 1
        elif wall == Directions.N:
            self._north = 1
        else:
            return

    def get_visit(self) -> bool:
        return self._visited

    def set_visit(self) -> None:
        self._visited = True

    def get_hex(self) -> str:
        bits: list[int] = [self._west, self._south, self._east, self._north]
        int_value: int = int("".join(map(str, bits)), 2)
        hex_value: str = hex(int_value)
        return hex_value[2:]


class OriginCell(Cell):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self._next: OriginCell | None = None

    def get_next(self) -> "OriginCell | None":
        return self._next

    def set_next(self, next: "OriginCell") -> None:
        self._next = next

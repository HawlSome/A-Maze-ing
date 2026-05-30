# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 14:56:01 by varandri           ###   ########.fr      #
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
        self._protected: bool = False
        # self._next: "Cell | None" = None

    def get_coordinate(self) -> tuple[int, int]:
        return self._coordinate

    def open_wall(self, wall: Directions) -> None:
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

    def set_visit(self) -> None:
        self._visited = True

    def set_protect(self) -> None:
        self._protected = not self._protected

    def get_visit(self) -> bool:
        return self._visited

    def get_protect(self) -> bool:
        return self._protected

    def get_walls(self) -> tuple[int, int, int, int]:
        """Give a tuple of the walls of one cell in order (W, S, E, N)
        Returns:
            tuple[int, int, int, int]
        """
        return (
            self._west,
            self._south,
            self._east,
            self._north
        )

    def get_hex(self) -> str:
        bits: list[int] = [self._west, self._south, self._east, self._north]
        int_value: int = int("".join(map(str, bits)), 2)
        # if self.get_visit():
        #     int_value = 0
        hex_value: str = hex(int_value)
        return hex_value[2:]

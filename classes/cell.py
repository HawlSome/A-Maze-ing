# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 14:00:46 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Cell:
    def __init__(self, coordinate: tuple[int, int] = (0, 0)) -> None:
        self._coordinate: tuple[int, int] = coordinate
        self._north: int = 1
        self._south: int = 1
        self._west: int = 1
        self._east: int = 1
        self._isolation: bool = False

    def get_coordinate(self) -> tuple[int, int]:
        return self._coordinate

    def open_wall(self, wall: str = "") -> None:
        wall = wall.lower()
        if self._isolation:
            return
        if wall == "west":
            self._west = 0
        elif wall == "south":
            self._south = 0
        elif wall == "east":
            self._east = 0
        elif wall == "north":
            self._north = 0
        else:
            return

    def close_wall(self, wall: str = "") -> None:
        wall = wall.lower()
        if self._isolation:
            return
        if wall == "west":
            self._west = 1
        elif wall == "south":
            self._south = 1
        elif wall == "east":
            self._east = 1
        elif wall == "north":
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

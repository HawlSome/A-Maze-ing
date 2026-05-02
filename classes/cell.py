#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 16:06:32 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from enum import IntFlag


class Wall(IntFlag):
    NORTH = 0b0001
    EAST = 0b0010
    SOUTH = 0b0100
    WEST = 0b1000

    def opposite(self) -> "Wall":
        opposites = {
            Wall.NORTH: Wall.SOUTH,
            Wall.SOUTH: Wall.NORTH,
            Wall.EAST: Wall.WEST,
            Wall.WEST: Wall.EAST
        }
        return opposites[self]


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.coordinate: tuple[int, int] = (row, col)
        self.walls = Wall.NORTH | Wall.EAST | Wall.WEST | Wall.SOUTH
        self.visited = False

    def has_wall(self, direction: "Wall") -> bool:
        return bool(self.walls & direction)

    def walls_open(self) -> list["Wall"]:
        return [wall for wall in
                [Wall.NORTH, Wall.SOUTH, Wall.EAST, Wall.WEST]
                if not self.has_wall(wall)]

    def open_wall(self, direction: "Wall") -> None:
        self.walls = self.walls & ~direction

    def close_wall(self, direction: "Wall") -> None:
        self.walls = self.walls | direction

    def get_hex(self) -> str:
        hex_value = hex(self.walls)
        return hex_value[2:].upper()

    def __repr__(self) -> str:
        return f"{self.get_hex()}"
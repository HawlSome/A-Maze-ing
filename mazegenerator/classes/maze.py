#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:46:18 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 20:13:40 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .cell import Cell
from ..functions import generate_cells
from ..patterns import forty_two
from typing import Any


class Maze:
    def __init__(self, config: dict[str, Any]) -> None:
        w, h = (config["width"], config["height"])
        self._pattern_cells: list[tuple[int, int]] = []
        self.set_cells(w, h)
        self.set_pattern(w, h)
        self.set_entry(config["entry"])
        self.set_exit(config["exit"])
        self.__validate__()

    def __validate__(self) -> None:
        if (self._entry == self._exit):
            raise Exception("Entry and Exit can't be on the same place")
        en_x, en_y = self._entry
        ex_x, ex_y = self._exit
        ent_ext = (
            self._cells[en_y][en_x],
            self._cells[ex_y][ex_x]
        )
        for cell in ent_ext:
            if cell.get_protect():
                raise Exception(
                    f"ENTRY or EXIT overlapping the Pattern cells "
                    f"at {cell.get_coordinate()}"
                )

    def set_cells(self, w: int, h: int) -> None:
        self._cells: list[list[Cell]] = generate_cells(w, h)

    def set_pattern(self, w: int, h: int) -> None:
        pattern: list[list[str]] = forty_two
        w_pattern: int
        h_pattern: int
        w_pattern, h_pattern = (
            len(pattern[0]),
            len(pattern)
        )
        if w < (w_pattern + 1) or h < (h_pattern + 1):
            print(
                f"Pattern dimension {w_pattern}x{h_pattern} is too big for"
                f" the maze dimension {w}x{h}"
            )
            return
        x_start: int = (w - w_pattern) // 2
        y_start: int = (h - h_pattern) // 2
        for y in range(h_pattern):
            for x in range(w_pattern):
                if pattern[y][x] != " ":
                    self._cells[y_start + y][x_start + x].set_protect()
                    self._pattern_cells.append((x_start + x, y_start + y))

    def set_entry(self, entry_coordinate: tuple[int, int]) -> None:
        self._entry: tuple[int, int] = entry_coordinate

    def set_exit(self, exit_coordinate: tuple[int, int]) -> None:
        self._exit: tuple[int, int] = exit_coordinate

    def get_cells(self) -> list[list[Cell]]:
        return self._cells

    def get_entry(self) -> tuple[int, int]:
        return self._entry

    def get_exit(self) -> tuple[int, int]:
        return self._exit

    def get_pattern_cells(self) -> list[tuple[int, int]]:
        return self._pattern_cells

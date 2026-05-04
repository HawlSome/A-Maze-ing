# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:46:18 by varandri            #+#    #+#            #
#   Updated: 2026/05/03 14:46:21 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .cell import Cell, OriginCell
from ..utils import generate_cells
from ..patterns import forty_two
from typing import Any
import sys


class Maze:
    def __init__(self, config: dict[str, Any]) -> None:
        try:
            w: int
            h: int
            w, h = (config["width"], config["height"])
            algo: str | None = config.get("algorithm")
            self.set_cells(w, h, algo)
            self.set_pattern(w, h)
            self.set_entry(config["entry"])
            self.set_exit(config["exit"])

            if (self._entry == self._exit):
                raise Exception("Entry and Exit can't be on the same place")
            en_x: int
            en_y: int
            en_x, en_y = self._entry
            ex_x: int
            ex_y: int
            ex_x, ex_y = self._exit
            ent_ext = (
                self._cells[en_y][en_x],
                self._cells[ex_y][ex_x]
            )
            for cell in ent_ext:
                if cell.get_visit():
                    raise Exception(
                        f"ENTRY or EXIT overlapping the Pattern cells "
                        f"at {cell.get_coordinate()}"
                    )
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

    def set_cells(self, w: int, h: int, algo: str | None) -> None:
        if algo and algo in "origin shift":
            self._cells: list[list[Cell]] | list[list[OriginCell]] = \
                generate_cells(w, h, "origin")
        else:
            self._cells = generate_cells(w, h)

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
                    self._cells[y_start + y][x_start + x].set_visit()

    def set_entry(self, entry_coordinate: tuple[int, int]) -> None:
        self._entry: tuple[int, int] = entry_coordinate

    def set_exit(self, exit_coordinate: tuple[int, int]) -> None:
        self._exit: tuple[int, int] = exit_coordinate

    def get_cells(self) -> list[list[Cell]] | list[list[OriginCell]]:
        return self._cells

    def get_entry(self) -> tuple[int, int]:
        return self._entry

    def get_exit(self) -> tuple[int, int]:
        return self._exit

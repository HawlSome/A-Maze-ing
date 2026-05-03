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
            self.set_entry(config["entry"])
            self.set_exit(config["exit"])
            if (self._entry == self._exit):
                raise Exception("Entry and Exit can't be on the same place")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

    def set_cells(self, w: int, h: int, algo: str | None) -> None:
        if algo and algo in "origin shift":
            self._cells: list[list[Cell]] | list[list[OriginCell]] = \
                generate_cells(w, h, "origin")
        else:
            self._cells = generate_cells(w, h)

    def set_entry(self, entry_coordinate: tuple[int, int]) -> None:
        self._entry: tuple[int, int] = entry_coordinate

    def set_exit(self, exit_coordinate: tuple[int, int]) -> None:
        self._exit: tuple[int, int] = exit_coordinate

    def set_pattern(self, w: int, h: int) -> None:
        min

    def get_cells(self) -> list[list[Cell]] | list[list[OriginCell]]:
        return self._cells

    def get_entry(self) -> tuple[int, int]:
        return self._entry

    def get_exit(self) -> tuple[int, int]:
        return self._exit

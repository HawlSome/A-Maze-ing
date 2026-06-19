#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:46:18 by varandri            #+#    #+#            #
#   Updated: 2026/06/19 23:55:31 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .cell import Cell
from ..functions import generate_cells
from ..patterns import forty_two
from typing import Any


class Maze:
    """Represents a rectangular maze grid.

    Manages a grid of cells, tracks entry and exit points, applies
    pattern overlays (the 42 school logo), and provides access
    to the maze cells for generation and solving algorithms.
    """
    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize a maze from a configuration dictionary.

        Args:
            config (dict[str, Any]): Configuration with keys:
                - width (int): Maze grid width.
                - height (int): Maze grid height.
                - entry (tuple[int, int]): Starting cell coordinates.
                - exit (tuple[int, int]): Goal cell coordinates.
                - output_file (str, optional): Output filename
                (default: "maze.txt").

        Raises:
            Exception: If its own validation fails.
        """
        w, h = (config["width"], config["height"])
        self._output_file: str = config.get("output_file", "maze.txt")
        self._pattern_cells: list[tuple[int, int]] = []
        self.set_cells(w, h)
        self.set_pattern(w, h)
        self.set_entry(config["entry"])
        self.set_exit(config["exit"])
        self.__validate__()

    def __validate__(self) -> None:
        """Validate that entry and exit are valid and non-overlapping
        the cells in the 42 pattern.

        Raises:
            Exception: If entry or exit overlaps a protected cell.
        """
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
        """Initialize the maze grid with empty cells.

        Args:
            w (int): Grid width.
            h (int): Grid height.
        """
        self._cells: list[list[Cell]] = generate_cells(w, h)

    def set_pattern(self, w: int, h: int) -> None:
        """Apply a pattern (the 42 school logo) to the maze center.

        Marks pattern cells as protected so they cannot be carved by
        generation algorithms.

        Args:
            w (int): Grid width.
            h (int): Grid height.
        """
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
        """Set the entry point (starting cell) for the maze.

        Args:
            entry_coordinate (tuple[int, int]): (x, y) coordinates of entry.
        """
        self._entry: tuple[int, int] = entry_coordinate

    def set_exit(self, exit_coordinate: tuple[int, int]) -> None:
        """Set the exit point (goal cell) for the maze.

        Args:
            exit_coordinate (tuple[int, int]): (x, y) coordinates of exit.
        """
        self._exit: tuple[int, int] = exit_coordinate

    def get_cells(self) -> list[list[Cell]]:
        """Return the maze grid.

        Returns:
            list[list[Cell]]: 2D array of cells indexed as [y][x].
        """
        return self._cells

    def get_entry(self) -> tuple[int, int]:
        """Return the entry point coordinates.

        Returns:
            tuple[int, int]: (x, y) coordinates of the entry cell.
        """
        return self._entry

    def get_exit(self) -> tuple[int, int]:
        """Return the exit point coordinates.

        Returns:
            tuple[int, int]: (x, y) coordinates of the exit cell.
        """
        return self._exit

    def get_pattern_cells(self) -> list[tuple[int, int]]:
        """Return all protected pattern cell coordinates.

        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates
            that are protected.
        """
        return self._pattern_cells

    def get_output_file(self) -> str:
        """Return the configured output filename for the maze.

        Returns:
            str: Output filename.
        """
        return self._output_file

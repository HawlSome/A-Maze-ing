#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 14:29:07 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .directions import Directions


class Cell:
    """Represents a single cell in a maze grid.

    Each cell has four walls (north, south, east, west) represented as
    binary values (1 = wall closed, 0 = wall open). Cells track visited
    and protected states for maze generation and pattern placement.
    """
    def __init__(self, x: int, y: int) -> None:
        """Initialize a cell at the given grid coordinates.

        Args:
            x (int): X-coordinate in the grid.
            y (int): Y-coordinate in the grid.
        """
        self._coordinate: tuple[int, int] = (x, y)
        self._north: int = 1
        self._south: int = 1
        self._west: int = 1
        self._east: int = 1
        self._visited: bool = False
        self._protected: bool = False

    def get_coordinate(self) -> tuple[int, int]:
        """Return the (x, y) grid coordinates of the cell.

        Returns:
            tuple[int, int]: the (x, y) coordinates.
        """
        return self._coordinate

    def open_wall(self, wall: Directions) -> None:
        """Remove a wall in the specified direction.

        Args:
            wall (Directions): Direction of the wall to open (W, S, E, N).
        """
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
        """Add a wall in the specified direction.

        Args:
            wall (Directions): Direction of the wall to close (W, S, E, N).
        """
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

    def has_wall(self, wall: Directions) -> (int | None):
        """Check if a wall exists in the specified direction.

        Args:
            wall (Directions): Direction to check (W, S, E, N).

        Returns:
            int | None: 1 if wall exists, 0 if open, None if invalid direction.
        """
        if wall == Directions.W:
            return self._west
        elif wall == Directions.S:
            return self._south
        elif wall == Directions.E:
            return self._east
        elif wall == Directions.N:
            return self._north
        else:
            return None

    def set_visit(self) -> None:
        """Toggle the visited state of the cell."""
        self._visited = not self._visited

    def set_protect(self) -> None:
        """Mark the cell as protected (part of the pattern)."""
        self._protected = True

    def get_visit(self) -> bool:
        """Return whether the cell has been visited.

        Returns:
            bool: True if visited, False otherwise.
        """
        return self._visited

    def get_protect(self) -> bool:
        """Return whether the cell is protected.

        Returns:
            bool: True if protected, False otherwise.
        """
        return self._protected

    def get_walls(self) -> tuple[int, int, int, int]:
        """Return a tuple of wall states in order (W, S, E, N).

        Returns:
            tuple[int, int, int, int]: Wall states where 1=closed, 0=open.
        """
        return (
            self._west,
            self._south,
            self._east,
            self._north
        )

    def get_hex(self) -> str:
        """Return a hexadecimal representation of the cell's wall state.

        The four wall bits are packed into a single hex digit.
        North is the LSB and west as the MSB
        (e.g: 3 (binary 0011) means walls are open to the south and west)

        Returns:
            str: A hex string (0-f) representing the wall configuration.
        """
        bits: list[int] = [self._west, self._south, self._east, self._north]
        int_value: int = int("".join(map(str, bits)), 2)
        hex_value: str = hex(int_value)
        return hex_value[2:]

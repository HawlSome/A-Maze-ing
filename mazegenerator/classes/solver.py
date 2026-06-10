#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   solver.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/10 05:47:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 13:44:31 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .maze import Maze
from .directions import Directions


class Solution:
    """Represents a solution to a maze.

    Tracks the algorithm used and stores solving steps and direction
    sequences.
    """
    def __init__(
            self, maze: Maze, algorithm: str | None = None
    ) -> None:
        """Initialize a solution for the given maze.

        Args:
            maze (Maze): The maze intsance to solve.
            algorithm (str | None): Name of the solving algorithm used.
        """
        self._map: Maze = maze
        self._algorithm: str | None = algorithm
        self._solving_steps: list[
            tuple[tuple[int, int], tuple[int, int]]
        ] = []
        self._solutions: list[Directions] = []

    def get_solving_step(
            self
    ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        """Return the sequence of steps taken during solving.

        Returns:
            list[tuple[tuple[int,int], tuple[int,int]]]: List of cell
            coordinate pairs representing the solution path.
        """
        return (self._solving_steps)

    def get_solutions(self) -> list[Directions]:
        """Return the sequence of direction moves in the solution.

        Returns:
            list[Directions]: List of direction values representing
            movement from start to exit.
        """
        return (self._solutions)

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 22:26:50 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# from .utils import (
#     Maze, Solution, Directions, Cell,
#     prims
# )
from .utils import (
    Maze, Solution, Directions, Cell, prims_carver
)
from typing import Any


class MazeGenerator:
    def __init__(self, config: dict[str, Any]) -> None:
        self._map: Maze = Maze(config)
        self._algorithm: str | None = config.get("algorithm")
        self._seed: int | None = config.get("seed")
        self._perfection: bool | None = config.get("perfect")
        self._gen_steps: list[
            (tuple[tuple[int, int], tuple[int, int]] | None)
        ] = []
        self.maze_generate()
        self.maze_solve(config)

    def get_cell_walls(self, x: int, y: int) -> tuple[int, int, int, int]:
        """Get the walls of one cell in the coordinate (x, y) in the maze,
        int the order of (W, S, E, N)
        Args:
            x (int): the x coordinate of the cell.
            y (int): the y coordinate of the cell.
        Returns:
            tuple[int, int, int, int]
        """
        cells: list[list[Cell]] = self._map.get_cells()
        return (cells[y][x].get_walls())

    def get_maze_entry(self) -> tuple[int, int]:
        """Get the coordinate of the entry point of the current maze.
        Return:
            tuple[int, int]
        """
        return self._map.get_entry()

    def get_maze_exit(self) -> tuple[int, int]:
        """Get the coordinate of the exit point of the current maze.
        Return:
            tuple[int, int]
        """
        return self._map.get_exit()

    def maze_generate(self) -> None:
        self._gen_steps = prims_carver(self._map, self._seed, self._perfection)

    def maze_solve(self, config: dict[str, Any]) -> None:
        algorithm: str | None = config.get("solver_algorithm")
        self._solution: Solution = Solution(self._map, algorithm)

    def get_generation_step(
            self
    ) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
        """Get the steps of the generation of the maze.
        Returns:
            steps (list[(tuple[tuple[int, int], tuple[int, int]] | None)]):
            list of steps of the generations of the maze , the list is a list
            of two connected cell.
        """
        return self._gen_steps

    def get_solving_step(
            self
    ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        solution: Solution = self._solution
        return (solution.get_solving_step())

    def get_solution(self) -> list[Directions]:
        solution: Solution = self._solution
        return (solution.get_solutions())

    def get_pattern_cells(self) -> list[tuple[int, int]]:
        return self._map.get_pattern_cells()

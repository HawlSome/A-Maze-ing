# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 12:32:23 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze, Solution, Directions, Cell
from .algorithms import prims
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
        self.set_generation()
        self.set_solution(config)

    def set_generation(self) -> None:
        self._gen_steps = prims(self._map, self._seed, self._perfection)

    def set_solution(self, config: dict[str, Any]) -> None:
        algorithm: str | None = config.get("solver_algorithm")
        self._solution: Solution = Solution(self._map, algorithm)

    def get_generation_step(
            self
    ) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
        return self._gen_steps

    def get_solving_step(
            self
    ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        solution: Solution = self._solution
        return (solution.get_solving_step())

    def get_solution(self) -> list[Directions]:
        solution: Solution = self._solution
        return (solution.get_solutions())

    def get_walls(self, x: int, y: int) -> tuple[int, int, int, int]:
        cells: list[list[Cell]] = self._map.get_cells()
        return (cells[y][x].get_walls())

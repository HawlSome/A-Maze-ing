#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/09 12:00:07 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze, Cell
from .algorithms.dfs import gen_imperfect_maze, gen_perfect_maze
from typing import Any

class MazeGenerator:
    def __init__(self, config: dict[str, Any]) -> None:
        self._map: Maze = Maze(config)
        self._perfection: bool | None = config.get("perfect")
        self._gen_steps: list[list[Cell]] | None = []
        self.generate()

    def generate(self) -> None:
        if self._perfection:
            self._gen_steps = gen_perfect_maze(self._map.get_cells())
        else:
            self._gen_steps = gen_imperfect_maze(self._map.get_cells(), 0.2)

    def get_generation(self) -> list[list[Cell]] | None:
        return self._gen_steps
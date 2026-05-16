#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/16 10:48:45 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze
from .algorithms import prims, dfs, a_star
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
        self._path: list[tuple[int, int]] = []
        self.generate()
        self.find_path()

    def generate(self) -> None:
        if self._algorithm == "prims":
            self._gen_steps = prims(self._map, self._seed, self._perfection)
        else:
            self._gen_steps = dfs(self._map, self._seed, self._perfection)

    def find_path(self) -> None:
        self._path = a_star(self._map)

    def set_path(
            self, steps: list[tuple[int, int]]
    ) -> None:
        self._path = steps

    def set_generation(
            self, moves: list[
                (tuple[tuple[int, int], tuple[int, int]] | None)
            ]
    ) -> None:
        self._gen_steps = moves

    def get_generation(
            self
    ) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
        return self._gen_steps

    def get_path(
            self
    ) -> list[tuple[int, int]]:
        return self._path

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/06 14:02:07 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze
from .algorithms import prims
from typing import Any


class MazeGenerator:
    def __init__(self, config: dict[str, Any]) -> None:
        self._map: Maze = Maze(config)
        self._algorithm: str | None = config.get("algotithm")
        self._seed: int | None = config.get("seed")
        self._perfection: bool | None = config.get("perfect")
        self._gen_steps: list[
            (tuple[tuple[int, int], tuple[int, int]] | None)
        ] = []
        self.generate()

    def generate(self) -> None:
        self._gen_steps = prims(self._map, self._seed, self._perfection)

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

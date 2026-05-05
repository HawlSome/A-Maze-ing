# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/05 14:06:09 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze


class MazeGenerator:
    def __init__(self, seed: int | None = None) -> None:
        self._map: Maze = Maze({"1": "", "2": 1})
        self._algorithm: str = "prims"
        self._seed: int | None = seed
        self._perfection = False
        self._gen_steps: list[
            (tuple[tuple[int, int], tuple[int, int]] | None)
        ] = []

        if seed:
            self._seed = int(seed)

    def generate(self) -> None:
        pass

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

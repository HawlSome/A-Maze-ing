# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   solver.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/10 05:47:09 by varandri            #+#    #+#            #
#   Updated: 2026/05/10 06:41:58 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .maze import Maze
from .directions import Directions


class Solution:
    def __init__(
            self, maze: Maze, algorithm: str | None = None
    ) -> None:
        self._map: Maze = maze
        self._algorithm: str | None = algorithm
        self._solving_steps: list[
            tuple[tuple[int, int], tuple[int, int]]
        ] = []
        self._solutions: list[Directions] = []

    def get_solving_step(
            self
    ) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        return (self._solving_steps)

    def get_solutions(self) -> list[Directions]:
        return (self._solutions)

# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/05/03 14:59:35 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes import Maze
import random


class MazeGenerator:
    def __init__(self) -> None:
        self._map: Maze = Maze({"1": "", "2": 1})
        self._algorithm: str = "prims"
        self._seed: int | None
        self._perfection = False


__all__ = [
    "random"
]

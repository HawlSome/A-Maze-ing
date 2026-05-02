# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 16:47:47 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 17:15:49 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from packages import Any, Callable
from .cell import Cell
from utils import generate_cells


class Maze:
    def __init__(self, config: dict[str, Any]) -> None:

        self.cells: list[list["Cell"]] = generate_cells(
            config["WIDTH"], config["HEIGHT"]
        )

    def generate(self, algo: Callable[[Any], Any]) -> None:
        pass

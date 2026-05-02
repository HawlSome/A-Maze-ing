#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   output.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 14:15:57 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 14:27:00 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell
from typing import Any


def save_output(grid: list[list["Cell"]], config: dict[str, Any]) -> None:
    with open(config['output_file'], 'w') as file:
        for j in range(config['height'] - 1):
                for i in range(config['width'] - 1):
                    file.write(grid[j][i].get_hex())
                file.write("\n")

#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   output.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 14:15:57 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 21:44:40 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell
from typing import Any


def save_output(grid: list[list["Cell"]], config: dict[str, Any]) -> None:
    with open(config['output_file'], 'w') as file:
        for y in range(config['height']):
            for x in range(config['width'] - 1):
                file.write(grid[y][x].get_hex())
            file.write("\n")

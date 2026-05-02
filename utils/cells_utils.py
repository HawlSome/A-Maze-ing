#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cells_utils.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 13:27:44 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 14:39:32 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell, Wall


def generate_cells(width: int, height: int) -> list[list["Cell"]]:
    return [[Cell(i,j) for i in range(width)] for j in range(height)]


def connect_cells(cell_a: "Cell", cell_b: "Cell",
                        direction: "Wall") -> None:
    cell_a.open_wall(direction)
    cell_b.open_wall(direction.opposite())

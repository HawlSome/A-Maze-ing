#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dfs.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 19:14:38 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/02 20:06:46 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes.cell import Cell
from utils.cells_utils import get_neighbors, connect_cells
import random


def dfs(actual_cell: "Cell", grid: list[list[Cell]]):
    actual_cell.visited = True

    neighbors = get_neighbors(actual_cell, grid)
    random.shuffle(neighbors)

    for neighbor_cell in neighbors:
        if not neighbor_cell.visited:
            connect_cells(actual_cell, neighbor_cell)
            dfs(neighbor_cell, grid)

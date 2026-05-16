#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   renderer.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/16 17:58:39 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/16 22:18:02 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .drawer import CellDrawer
from mazegenerator.classes import Directions


class MazeRenderer:
    def __init__(self,
                 img_data: memoryview,
                 cell_size: int,
                 wall_size: int,
                 width: int,
                 color: int = 0xFF0F0F0F) -> None:

        self.cell = CellDrawer(img_data, cell_size, wall_size, width, color)

    def draw_wall(self,
                  col: int,
                  row: int,
                  wall: Directions,
                  color: int) -> None:
        self.cell.color = color

        if wall == Directions.W:
            self.cell.draw_west(col, row)

        elif wall == Directions.E:
            self.cell.draw_east(col, row)

        elif wall == Directions.N:
            self.cell.draw_north(col, row)

        elif wall == Directions.S:
            self.cell.draw_south(col, row)

    def fill_cell(self,
                  col: int,
                  row: int,
                  color: int) -> None:
        self.cell.color = color

        self.cell.draw_rect(
            col * self.cell.cell_size,
            row * self.cell.cell_size,
            self.cell.cell_size,
            self.cell.cell_size
        )

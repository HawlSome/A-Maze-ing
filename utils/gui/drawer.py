#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   drawer.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/16 17:01:54 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/16 22:17:47 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class CellDrawer:
    def __init__(self,
                 img_data: memoryview,
                 cell_size: int,
                 wall_size: int,
                 width: int,
                 color: int) -> None:
        self.img = img_data
        self.cell_size = cell_size
        self.wall_size = wall_size
        self.width = width
        self.color = color

    def draw_rect(self,
                  start_x: int,
                  start_y: int,
                  rect_height: int,
                  rect_width: int) -> None:

        color = self.color.to_bytes(4, 'little')
        for y in range(start_y, start_y + rect_height):
            for x in range(start_x, start_x + rect_width):
                offset = y * self.width + x
                # self.img[offset:offset+4] = color
                for i in range(4):
                    self.img[offset * 4 + i] = color[i]

    def draw_west(self,
                  col: int, row: int) -> None:
        self.draw_rect(
            col * self.cell_size - self.wall_size,
            row * self.cell_size,
            self.cell_size,
            self.wall_size
        )

    def draw_east(self,
                  col: int, row: int) -> None:
        self.draw_rect(
            (col + 1) * self.cell_size - self.wall_size,
            row * self.cell_size,
            self.cell_size,
            self.wall_size
        )

    def draw_north(self,
                   col: int, row: int) -> None:
        self.draw_rect(
            col * self.cell_size,
            row * self.cell_size - self.wall_size,
            self.wall_size,
            self.cell_size
        )

    def draw_south(self,
                   col: int, row: int) -> None:
        self.draw_rect(
            col * self.cell_size,
            (row + 1) * self.cell_size - self.wall_size,
            self.wall_size,
            self.cell_size
        )

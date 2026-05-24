# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   drawer.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:28 by varandri            #+#    #+#            #
#   Updated: 2026/05/24 14:33:34 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class CellDrawer:
    def __init__(
            self, img: memoryview, color: int, grid_with: int, cell_size: int,
            wall_size: int
    ) -> None:
        self._img: memoryview = img
        self._color: int = color
        self._grid_with: int = grid_with
        self._cell_size: int = cell_size
        self._wall_size: int = wall_size

    def _draw_line(
        self, start_x: int, start_y: int,
        end_x: int, end_y: int,
    ) -> None:
        """A method for drawing a line in raw pixel"""
        color: bytes = self._color.to_bytes(4, 'little')
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                pixel = y * self._grid_with + x

                for i in range(4):
                    self._img[pixel * 4 + i] = color[i]

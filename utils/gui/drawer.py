#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   drawer.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:28 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 23:45:24 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class CellDrawer:
    def __init__(
            self, img: memoryview, color: int, grid_width: int,
            cell_pixel_size: int, wall_pixel_size: int
    ) -> None:
        self._img: memoryview = img
        self._color: int = color
        self._grid_width: int = grid_width
        self._cell_pixel_size: int = cell_pixel_size
        self._wall_pixel_size: int = wall_pixel_size

    def set_color(self, color: int) -> None:
        self._color = color

    def get_img(self) -> memoryview:
        return self._img

    def get_grid_width(self) -> int:
        return self._grid_width

    def get_cell_pixel_size(self) -> int:
        return self._cell_pixel_size

    def get_wall_pixel_size(self) -> int:
        return self._wall_pixel_size

    def draw_line(
        self, start_x: int, start_y: int,
        line_width: int, line_height: int,
    ) -> None:
        """Draw a filled rectangle of pixels directly into the image buffer.

        Args:
            start_x (int): Horizontal starting position in pixels (left edge).
            start_y (int): Vertical starting position in pixels (top edge).
            line_width (int): Width of the rectangle in pixels.
            line_height (int): Height of the rectangle in pixels.

        Returns:
            None
        """
        color: bytes = self._color.to_bytes(4)
        for y in range(start_y, start_y + line_height):
            for x in range(start_x, start_x + line_width):
                pixel = y * self._grid_width + x

                for i in range(4):
                    self._img[pixel * 4 + i] = color[i]

    def draw_west(
        self, col: int, row: int
    ) -> None:
        """Draw a filled rectangle of pixels in the WEST side of a cell.
            Args:
                col (int): the starting point in the column range.
                row (int): the starting point in the row range.
            Returns:
                None
        """
        if col > 0:
            col = col * self._cell_pixel_size - self._wall_pixel_size
        if row > 0:
            row = row * self._cell_pixel_size - self._wall_pixel_size
        self.draw_line(
            start_x=col,
            start_y=row,
            line_width=self._wall_pixel_size,
            line_height=self._cell_pixel_size
        )

    def draw_south(
        self, col: int, row: int
    ) -> None:
        """Draw a filled rectangle of pixels in the SOUTH side of a cell.
            Args:
                col (int): the starting point in the column range.
                row (int): the starting point in the row range.
            Returns:
                None
        """
        self.draw_line(
            start_x=col * self._cell_pixel_size,
            start_y=(row + 1) * self._cell_pixel_size - self._wall_pixel_size,
            line_width=self._cell_pixel_size,
            line_height=self._wall_pixel_size
        )

    def draw_east(
        self, col: int, row: int
    ) -> None:
        """Draw a filled rectangle of pixels in the EAST side of a cell.
            Args:
                col (int): the starting point in the column range.
                row (int): the starting point in the row range.
            Returns:
                None
        """
        self.draw_line(
            start_x=(col + 1) * self._cell_pixel_size - self._wall_pixel_size,
            start_y=row * self._cell_pixel_size,
            line_width=self._wall_pixel_size,
            line_height=self._cell_pixel_size
        )

    def draw_north(
        self, col: int, row: int
    ) -> None:
        """Draw a filled rectangle of pixels in the NORTH side of a cell.
            Args:
                col (int): the starting point in the column range.
                row (int): the starting point in the row range.
            Returns:
                None
        """
        if row > 0:
            row = row * self._cell_pixel_size - self._wall_pixel_size
        self.draw_line(
            start_x=col * self._cell_pixel_size,
            start_y=row,
            line_width=self._cell_pixel_size,
            line_height=self._wall_pixel_size,
        )

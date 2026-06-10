#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   renderer.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:07:56 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 14:28:03 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .colors import transparent, black, white


class Renderer:
    """Draws maze cells and walls into a pixel buffer.

    The renderer operates on a contiguous image buffer (memoryview)
    that represents a 2D RGBA image. It exposes helpers to draw
    filled pixel rectangles, fill cells and draw the walls for a
    given cell coordinate.
    """
    def __init__(
            self, img: memoryview, img_width: int, img_height: int,
            cell_pixel_size: int, wall_pixel_size: int,
            cell_color: int = black
    ):
        """Initialize a `Renderer` instance.

        Args:
            img (memoryview): Backing image buffer (RGBA bytes).
            img_width (int): Width of the image in pixels.
            img_height (int): Height of the image in pixels.
            cell_pixel_size (int): Size of a maze cell in pixels.
            wall_pixel_size (int): Thickness of walls in pixels.
            cell_color (int): Default color used to fill cells.
        """
        self._img: memoryview = img
        self._img_width: int = img_width
        self._img_height: int = img_height
        self._cell_pixel_size: int = cell_pixel_size
        self._wall_pixel_size: int = wall_pixel_size
        self._cell_color: int = cell_color
        self._wall_color: int = transparent

    def _draw_pixel(
            self, start_x: int, start_y: int,
            pixel_width: int, pixel_height: int,
            pixel_color: int
    ) -> None:
        """Draw a filled rectangle of pixels directly into the image buffer.

        Args:
            start_x (int): Horizontal starting position in pixels (left edge).
            start_y (int): Vertical starting position in pixels (top edge).
            pixel_width (int): Width of the rectangle in pixels.
            pixel_height (int): Height of the rectangle in pixels.
            pixel_color (int): The color to paint the line.
        """
        color: bytes = pixel_color.to_bytes(4)
        for y in range(start_y, start_y + pixel_height):
            for x in range(start_x, start_x + pixel_width):
                pixel = y * (self._img_width) + x

                for i in range(4):
                    self._img[pixel * 4 + i] = color[i]

    def _draw_west(self, x: int, y: int) -> None:
        """Draw a filled rectangle of pixels in the WEST side of a cell.

            Args:
                x (int): the starting point in the x range.
                y (int): the starting point in the y range.
        """
        self._draw_pixel(
            start_x=x * self._cell_pixel_size,
            start_y=y * self._cell_pixel_size,
            pixel_width=self._wall_pixel_size,
            pixel_height=self._cell_pixel_size,
            pixel_color=self._wall_color
        )

    def _draw_east(self, x: int, y: int) -> None:
        """Draw a filled rectangle of pixels in the WEST side of a cell.

            Args:
                x (int): the starting point in the x range.
                y (int): the starting point in the y range.
        """
        x_value: int = (x + 1) * self._cell_pixel_size
        if x_value >= self._img_width:
            x_value -= self._wall_pixel_size
        self._draw_pixel(
            start_x=x_value,
            start_y=y*self._cell_pixel_size,
            pixel_width=self._wall_pixel_size,
            pixel_height=self._cell_pixel_size,
            pixel_color=self._wall_color,
        )

    def _draw_north(self, x: int, y: int) -> None:
        """Draw a filled rectangle of pixels in the WEST side of a cell.

            Args:
                x (int): the starting point in the x range.
                y (int): the starting point in the y range.
        """
        self._draw_pixel(
            start_x=x * self._cell_pixel_size,
            start_y=y * self._cell_pixel_size,
            pixel_width=self._cell_pixel_size,
            pixel_height=self._wall_pixel_size,
            pixel_color=transparent
        )

    def _draw_south(self, x: int, y: int) -> None:
        """Draw a filled rectangle of pixels in the WEST side of a cell.

            Args:
                x (int): the starting point in the x range.
                y (int): the starting point in the y range.
        """
        y_value: int = (y + 1) * self._cell_pixel_size
        if y_value >= self._img_height:
            y_value -= self._wall_pixel_size
        self._draw_pixel(
            start_x=x * self._cell_pixel_size,
            start_y=y_value,
            pixel_width=self._cell_pixel_size,
            pixel_height=self._wall_pixel_size,
            pixel_color=transparent
        )

    def fill_cell(
            self, x: int, y: int, walls: tuple[int, int, int, int],
            color: int
    ) -> None:
        """Function to fill a cell in a certain coordinate with color.

        Args:
            x (int): The x cooordinate of the cell to fill a color with.
            y (int): The y coordinate of the cell to fill a color with.
            walls (tuple[int, int, int,int]): The walls of the cell
                to fill color with.
            color (int): The color to fill the chosen cell with.
        """
        x_value: int = x * self._cell_pixel_size
        y_value: int = y * self._cell_pixel_size
        width_value: int = self._cell_pixel_size
        height_value: int = self._cell_pixel_size
        w, s, e, n = walls
        if w:
            x_value += self._wall_pixel_size
            width_value -= self._wall_pixel_size
        if n:
            y_value += self._wall_pixel_size
            height_value -= self._wall_pixel_size
        if e and (x + 1) * self._cell_pixel_size >= self._img_width:
            width_value -= self._wall_pixel_size
        if s and (y + 1) * self._cell_pixel_size >= self._img_height:
            height_value -= self._wall_pixel_size
        self._draw_pixel(
            start_x=x_value,
            start_y=y_value,
            pixel_width=width_value,
            pixel_height=height_value,
            pixel_color=color
        )

    def fill_img(self, color: int = white) -> None:
        """Function to fill an image with one color.

        Args:
            color (int): The color to fill the image with.
        """
        self._draw_pixel(
            start_x=0,
            start_y=0,
            pixel_width=self._img_width,
            pixel_height=self._img_height,
            pixel_color=color
        )

    def draw_cell(
            self, x: int, y: int,
            walls: tuple[int, int, int, int]
    ) -> None:
        """Function to draw a cell in a certain coordinate with color.

        Args:
            x (int): The x coordinate of the cell to draw.
            y (int): The y coordinate of the cell to draw.
            walls (tuple[int, int, int,int]): The walls of the cell
                to carve.
        """
        self.fill_cell(x, y, walls, self._cell_color)
        w, s, e, n = walls
        if w:
            self._draw_west(x, y)
        if s:
            self._draw_south(x, y)
        if e:
            self._draw_east(x, y)
        if n:
            self._draw_north(x, y)

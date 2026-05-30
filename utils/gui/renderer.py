#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   renderer.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:31 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 23:38:46 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .drawer import CellDrawer


class MazeRenderer:
    """Renders maze walls and cells into a pixel image buffer.

    Delegates all pixel-level drawing to a CellDrawer instance,
    providing a higher-level interface for filling cells and drawing
    directional walls by color.

    Args:
        img_data (memoryview): The raw image buffer to draw into.
        cell_pixel_size (int): Width and height of each cell in pixels.
        wall_pixel_size (int): Thickness of each wall in pixels.
        grid_width (int): Width of the image grid in pixels.
        color (int): Default ARGB color for drawing. Defaults to 0xFF0F0F0F.
    """
    def __init__(
        self, img_data: memoryview, cell_pixel_size: int,
        wall_pixel_size: int, grid_width: int, color: int = 0x00000000
    ) -> None:
        self._cell: CellDrawer = CellDrawer(
            img=img_data,
            color=color,
            grid_width=grid_width,
            cell_pixel_size=cell_pixel_size,
            wall_pixel_size=wall_pixel_size
        )

    def draw_wall(
            self, col: int, row: int, walls: tuple[int, int, int, int],
            color: int = 0x00000000
    ) -> None:
        """Function to draw a colored wall in a coordinate of row and column
        of a cell.

        Args:
            col (int): the column of the cell to draw a wall.
            row (int): the row of the cell to draw a wall.
            walls (tuple[int, int, int, int]): the values of
            the walls of the cells in oreder of "W, S, E, N" and the value
            is between (0 | 1).
            color (int): the color to draw the line. Default to 0x00000000

        Raises:
            ValueError: If wall is none of 'w', 's', 'e', 'n'.

        Returns:
            None.
        """
        self._cell.set_color(color)
        w, s, e, n = walls
        if w:
            self._cell.draw_west(col, row)
        if s:
            self._cell.draw_south(col, row)
        if e:
            self._cell.draw_east(col, row)
        if n:
            self._cell.draw_north(col, row)

    def fill_cell(self, col: int, row: int, color: int) -> None:
        """Function to fill a cell in a certain coordinate with color.

        Args:
            col (int): the colum of the cell to fill a color with.
            row (int): the row of the cell to fill a color with.
            color (int): the color to fill the chosen cell with.

        Returns:
            None.
        """
        self._cell.set_color(color)
        self._cell.draw_line(
            start_x=col * self._cell.get_cell_pixel_size(),
            start_y=row * self._cell.get_cell_pixel_size(),
            line_height=self._cell.get_cell_pixel_size(),
            line_width=self._cell.get_cell_pixel_size()
        )

    def fill_grid(self, color: int, grid_width: int, grid_height: int) -> None:
        """Function to fill a the grid with one color.

            Args:
                col (int): the colum of the cell to fill a color with.
                grid_width (int): The width of the grid.
                grid_height (int): The height of the grid.
            Returns:
                None.
        """
        self._cell.set_color(color)
        self._cell.draw_line(
            start_x=0,
            start_y=0,
            line_width=grid_width,
            line_height=grid_height
        )

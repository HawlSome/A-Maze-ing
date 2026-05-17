#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   displayer.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/16 20:41:33 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/17 13:52:00 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .renderer import MazeRenderer
from mazegenerator.classes import Maze, Directions
from mlx import Mlx
from typing import Any
import time


class MazeDisplayer:
    def __init__(self,
                 cell_size: int,
                 wall_size: int,
                 win_width: int,
                 win_height: int) -> None:

        self.width = win_width
        self.height = win_height
        self._init_mlx()
        self._init_hooks()
        self.renderer = MazeRenderer(
            self.img_data, cell_size, wall_size, self.width)

    def _init_mlx(self):
        self.mlx: Mlx = Mlx()
        self.mlx_ptr: Any = self.mlx.mlx_init()
        self.win = self.mlx.mlx_new_window(
            self.mlx_ptr, self.width, self.height, "A-Maze-ing")
        self.img = self.mlx.mlx_new_image(
            self.mlx_ptr, self.width, self.height)
        self.img_data, _, _, _ = self.mlx.mlx_get_data_addr(self.img)

# hook the X button and esc (quit the window)
    def _init_hooks(self):
        def clean_exit(*args):
            self.mlx.mlx_destroy_window(self.mlx_ptr, self.win)
            self.mlx.mlx_destroy_image(self.mlx_ptr, self.img)
            self.mlx.mlx_loop_exit(self.mlx_ptr)

        def key_press(key: int, *args):
            if key == 0xFF1B:
                clean_exit()

        self.mlx.mlx_hook(self.win, 33, 0, clean_exit, None)
        self.mlx.mlx_key_hook(self.win, key_press, None)

# draw 42 pattern and entry, exit
    def draw_pattern(self,
                     colors: list[int],
                     maze: Maze) -> None:
        grid = maze.get_cells()
        width = len(grid[0])
        height = len(grid)

        for y in range(height):
            for x in range(width):
                cell = grid[y][x]

                if cell.get_protect():
                    self.renderer.fill_cell(x, y, colors[1])
                else:
                    continue

        s_x, s_y = maze.get_entry()
        e_x, e_y = maze.get_exit()
        self.renderer.fill_cell(s_x, s_y, colors[2])
        self.renderer.fill_cell(e_x, e_y, colors[2])

    def draw_maze_walls(self,
                        color: int,
                        maze: Maze,
                        moves: list[(tuple[tuple[int, int],
                                           tuple[int, int]] | None)]
                        ) -> None:
        grid = maze.get_cells()

        for move in moves:
            x, y = move[0]
            cell = grid[y][x]

            if cell.has_wall(Directions.W):
                self.renderer.draw_wall(x, y, Directions.W, color)

            if cell.has_wall(Directions.E):
                self.renderer.draw_wall(x, y, Directions.E, color)

            if cell.has_wall(Directions.N):
                self.renderer.draw_wall(x, y, Directions.N, color)

            if cell.has_wall(Directions.S):
                self.renderer.draw_wall(x, y, Directions.S, color)

            self.mlx.mlx_put_image_to_window(self.mlx_ptr,
                                             self.win, self.img, 0, 0)
            time.sleep(0.01)

    def display(self,
                colors: list[int],
                maze: Maze,
                moves: list[(tuple[tuple[int, int], tuple[int, int]] | None)]
                ) -> None:

        self.draw_maze_walls(colors[0], maze, moves)
        self.draw_pattern(colors, maze)
        self.mlx.mlx_put_image_to_window(self.mlx_ptr,
                                         self.win, self.img, 0, 0)
        self.mlx.mlx_loop(self.mlx_ptr)

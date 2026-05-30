#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   displayer.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:25 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 23:41:50 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# from threading import Thread, Event
from .ft_mlx import PyMlx, c_void_p
from .renderer import MazeRenderer
from mazegenerator import MazeGenerator
from typing import Any
from random import randint


class Static:
    checker: bool = True
    count = 0


class MazeDisplayer:
    def __init__(
        self, maze: MazeGenerator,
        win_width: int, win_height: int, bg_color: int,
        cell_pixel_size: int, wall_pixel_size: int
    ) -> None:
        self._maze: MazeGenerator = maze
        self._win_width: int = win_width
        self._win_height: int = win_height
        self._cell_pixel_size: int = cell_pixel_size
        self._wall_pizel_size: int = wall_pixel_size
        self._statics: Static = Static()
        self._mlx: PyMlx = PyMlx()
        self._init_window(win_width, win_height, bg_color)
        self._init_loop_hook()
        self._init_hooks(self._window)

    def _init_window(
        self, win_width: int, win_height: int,
        bg_color: int
    ) -> None:
        """Create a new main MLX window.
        Args:
            win_width (int): The width of the window.
            win_height (int): The height of the window.
            bg_color (int): The background color of the window (0x|RR|GG|BB|AA)
        Returns:
            None
        """
        self._window: c_void_p = self._mlx.new_window(
                                    win_width, win_height, "A-MAZE-ING"
                                )
        self._background: c_void_p = self._mlx.new_image(win_width, win_height)
        img_data: memoryview
        img_data, _, _, _ = self._mlx.get_data_addr(self._background)
        renderer: MazeRenderer = MazeRenderer(
            img_data,
            win_width,
            win_width,
            win_width,
            bg_color
        )
        renderer.fill_grid(bg_color, win_width, win_height)
        self._mlx.put_image_to_window(self._window, self._background, 0, 0)
        del (renderer)

    def _init_loop_hook(self) -> None:
        self._foreground: c_void_p = self._mlx.new_image(
            width=self._win_width,
            height=self._win_height
        )
        img_data: memoryview
        img_data, _, _, _ = self._mlx.get_data_addr(self._foreground)
        renderer: MazeRenderer = MazeRenderer(
            img_data,
            self._cell_pixel_size,
            self._wall_pizel_size,
            self._win_width,
        )
        renderer.fill_grid(0X000000FF, self._win_width, self._win_height)
        maze_steps: list[tuple[
            tuple[int, int], tuple[int, int]] |
            None
        ] = self._maze.get_generation_step()

        def crave_maze(params: list[Any]) -> None:
            renderer: MazeRenderer = params[0]
            maze_steps: list[tuple[
                tuple[int, int], tuple[int, int]] |
                None
            ] = params[1]
            if self._statics.checker:
                if len(maze_steps):
                    if maze_steps[0]:
                        if self._statics.count == 0:
                            x, y = maze_steps[0][0]
                        else:
                            x, y = maze_steps[0][1]
                    walls: tuple[int, int, int, int] = self._maze.get_walls(x, y)
                    renderer.draw_wall(x, y, walls)
                    if self._statics.count:
                        maze_steps.pop(0)
                    self._mlx.clear_window(self._window)
                    self._mlx.put_image_to_window(
                        self._window, self._background, 0, 0
                    )
                    self._mlx.put_image_to_window(
                        self._window, self._foreground, 0, 0
                    )
                    self._statics.count += 1
                else:
                    del (renderer)
                    self._statics.checker = False

        self._mlx.loop_hook(crave_maze, [renderer, maze_steps])

    def _init_hooks(self, win: c_void_p) -> None:
        """Initiate the events, the hooks and the main loop of the mlx instance
        Args:
            win (c_void_p): The address of the created window from mlx
        Returns:
            None
        """
        def safe_exit(data: None = None) -> None:
            if self._background:
                self._mlx.destroy_image(self._background)
            self._mlx.destroy_window(win)
            self._mlx.loop_exit()

        def change_color(data: None = None) -> None:
            img_data, _, _, _ = self._mlx.get_data_addr(self._background)
            r: int = randint(0, 255)
            g: int = randint(0, 255)
            b: int = randint(0, 255)
            color = (r << 24) | (g << 16) | (b << 8) | (0xFF)
            renderer: MazeRenderer = MazeRenderer(
                img_data,
                self._win_width,
                self._win_width,
                self._win_width,
                color
            )
            renderer.fill_grid(color, self._win_width, self._win_height)
            self._mlx.clear_window(self._window)
            self._mlx.put_image_to_window(self._window, self._background, 0, 0)
            self._mlx.put_image_to_window(self._window, self._foreground, 0, 0)
            del (renderer)

        def on_key(key: int, data: None = None) -> None:
            if key == 113:
                safe_exit()
            if key == 99:
                change_color()

        self._mlx.key_hook(self._window, on_key)
        self._mlx.hook(self._window, 33, 0, safe_exit)
        self._mlx.loop()
        self._mlx.release()

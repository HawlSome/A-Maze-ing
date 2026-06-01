#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   displayer.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:25 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 23:16:30 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .ft_mlx import PyMlx, c_void_p
from mazegenerator import MazeGenerator
from typing import Any
from .renderer import Renderer
from .colors import random_color, transparent


class Static:
    run: bool = True
    regenerate: bool = False
    default_pattern: bool = True
    count: int = 0


class MazeDisplayer:
    def __init__(
        self, config: dict[str, Any],
        win_width: int, win_height: int,
        cell_pixel_size: int, wall_pixel_size: int
    ) -> None:
        self._config: dict[str, Any] = config
        self._statics: Static = Static()
        self._mlx: PyMlx = PyMlx()
        self._maze: MazeGenerator = MazeGenerator(self._config)
        self._background: tuple[c_void_p, Renderer]
        self._foreground: tuple[c_void_p, Renderer]
        self._init_img(win_width, win_height, cell_pixel_size, wall_pixel_size)
        self._init_window(win_width, win_height)
        self._init_loop_hook()
        self._init_hooks(self._window)

    def _init_img(
            self, win_width: int, win_height: int,
            cell_pixel_size: int, wall_pixel_size: int
    ) -> None:
        mlx = self._mlx

        def init_background() -> None:
            bg: c_void_p = mlx.new_image(win_width, win_height)
            bg_data, _, _, _ = mlx.get_data_addr(bg)
            bg_renderer: Renderer = Renderer(
                bg_data, win_width, win_height,
                cell_pixel_size, wall_pixel_size,
            )
            bg_renderer.fill_img()
            self._background = (bg, bg_renderer)

        def init_foreground() -> None:
            fg: c_void_p = mlx.new_image(win_width, win_height)
            fg_data, _, _, _ = mlx.get_data_addr(fg)
            fg_renderer: Renderer = Renderer(
                fg_data, win_width, win_height,
                cell_pixel_size, wall_pixel_size,
            )
            fg_renderer.fill_img(transparent)
            self._foreground = (fg, fg_renderer)

        init_background()
        init_foreground()

    def _init_window(self, win_width: int, win_height: int) -> None:
        """Create a new main MLX window.
        Args:
            win_width (int): The width of the window.
            win_height (int): The height of the window.
        Returns:
            None
        """
        mlx: PyMlx = self._mlx
        self._window: c_void_p = mlx.new_window(
            win_width, win_height, "A-MAZE-ING"
        )
        bg, _ = self._background
        fg, _ = self._foreground
        mlx.put_image_to_window(self._window, bg, 0, 0)
        mlx.put_image_to_window(self._window, fg, 0, 0)

    def _init_loop_hook(self) -> None:
        statics: Static = self._statics
        fg, fg_renderer = self._foreground
        bg, _ = self._background
        mlx: PyMlx = self._mlx
        maze: MazeGenerator = self._maze
        maze_steps: list[tuple[
            tuple[int, int], tuple[int, int]] |
            None
        ] = maze.get_generation_step()
        pattern_cells: list[tuple[int, int]] = maze.get_pattern_cells()

        def refresh_window() -> None:
            mlx.clear_window(self._window)
            mlx.put_image_to_window(self._window, bg, 0, 0)
            mlx.put_image_to_window(self._window, fg, 0, 0)

        def regenerate(
            maze_steps: list[
                tuple[tuple[int, int], tuple[int, int]] | None
            ]
        ) -> None:
            self._maze = MazeGenerator(self._config)
            statics.run = True
            maze_steps.clear()
            statics.count = 0
            statics.default_pattern = True
            maze_steps.extend(self._maze.get_generation_step()[:])
            fg_renderer.fill_img(transparent)
            refresh_window()
            f = open("output_maze.py.txt", "w")
            f.close()
            statics.regenerate = False

        def carve_pattern() -> None:
            if not statics.default_pattern:
                color: int = random_color()
            else:
                try:
                    color = int(self._config["pattern_color"], 16)
                    if color > ((255 << 24) | (255 << 16) | (255 << 8) | 255):
                        raise ValueError
                except (KeyError, ValueError):
                    print(
                        "PATTERN_COLOR key - not found in config.txt "
                        "or Value out of bound"
                    )
                    color = random_color()
            cells: list[tuple[int, int]] = pattern_cells[:]
            for i in range(len(cells)):
                w, s, e, n = (1, 1, 1, 1)
                if (
                    i < len(cells) - 1 and
                    (cells[i][0] - cells[i + 1][0]) == -1
                ):
                    e = 0
                if i > 0 and (cells[i][0] - cells[i - 1][0]) == 1:
                    w = 0
                if i in (3, 4, 5, 8, 9, 12, 13):
                    s = 0
                if i in (4, 5, 6, 11, 12, 13, 14, 15):
                    n = 0
                fg_renderer.fill_cell(*cells[i], (w, s, e, n), color)

        def carve_maze(params: list[Any]) -> None:
            renderer = params[0]
            if statics.run:
                if len(maze_steps):
                    if maze_steps[0] and not statics.count:
                        x, y = maze_steps[0][0]
                    elif maze_steps[0] and statics.count:
                        x, y = maze_steps[0][1]
                    else:
                        maze_steps.pop(0)
                        return
                    walls: tuple[
                        int, int, int, int
                    ] = self._maze.get_cell_walls(x, y)
                    renderer.draw_cell(x, y, walls)
                    if statics.count:
                        maze_steps.pop(0)
                    refresh_window()
                    statics.count += 1
                else:
                    maze_entry: tuple[int, int] = self._maze.get_maze_entry()
                    maze_exit: tuple[int, int] = self._maze.get_maze_exit()
                    color = random_color()
                    renderer.fill_cell(*maze_entry, (1, 1, 1, 1), color)
                    renderer.fill_cell(*maze_exit, (1, 1, 1, 1), color)
                    carve_pattern()
                    refresh_window()
                    statics.run = False

            if statics.regenerate:
                regenerate(maze_steps)

        mlx.loop_hook(carve_maze, [fg_renderer, maze_steps])

    def _init_hooks(self, win: c_void_p) -> None:
        """Initiate the events, the hooks and the main loop of the mlx instance
        Args:
            win (c_void_p): The address of the created window from mlx
        Returns:
            None
        """
        mlx: PyMlx = self._mlx
        bg, bg_renderer = self._background
        fg, fg_renderer = self._foreground
        statics: Static = self._statics

        def safe_exit(data: None = None) -> None:
            if bg:
                mlx.destroy_image(bg)
            if fg:
                mlx.destroy_image(fg)
            mlx.destroy_window(win)
            mlx.loop_exit()

        def change_color(data: None = None) -> None:
            bg_renderer.fill_img(random_color())
            mlx.clear_window(self._window)
            mlx.put_image_to_window(self._window, bg, 0, 0)
            mlx.put_image_to_window(self._window, fg, 0, 0)

        def on_key(key: int, data: None = None) -> None:
            if key == 113:
                safe_exit()
            if key == 114:
                statics.run = False
                statics.regenerate = True
            if key == 99:
                statics.run = True
                statics.default_pattern = False
                change_color()

        mlx.key_hook(self._window, on_key)
        mlx.hook(self._window, 33, 0, safe_exit)
        mlx.loop()
        mlx.release()

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   displayer.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:25 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 12:23:05 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .ft_mlx import PyMlx, c_void_p
from mazegenerator import MazeGenerator
from typing import Any
from .renderer import Renderer
from .colors import random_color, transparent, black
from time import sleep


class Static:
    """Container of runtime flags used by the `MazeDisplayer` loop.

    Attributes:
        run (bool): Whether the generation loop should continue.
        regenerate (bool): Request for regenerating the maze.
        default_pattern (bool): Whether to use the default pattern color.
        count (int): Internal step counter used by the loop.
        show_path (bool): Whether the solution path should be drawn.
        run_path (bool): Whether to animate the path drawing.
    """
    run: bool = True
    regenerate: bool = False
    default_pattern: bool = True
    count: int = 0
    show_path: bool = True
    run_path: bool = False


class MazeDisplayer:
    def __init__(
        self, config: dict[str, Any],
        win_width: int, win_height: int,
        cell_pixel_size: int, wall_pixel_size: int
    ) -> None:
        """Create a GUI displayer for visualizing maze operations.

        Args:
            config (dict[str, Any]): Configuration dictionary read from
                the project's `config.txt` file.
            win_width (int): Window width in pixels.
            win_height (int): Window height in pixels.
            cell_pixel_size (int): Size of a maze cell in pixels.
            wall_pixel_size (int): Thickness of walls in pixels.
        """
        self._config: dict[str, Any] = config
        self._win_height = win_height
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
        """Allocate background and foreground image buffers.

        This initializes two separate image buffers: one for a static
        background and one for a foreground overlay. Each buffer is
        wrapped by a `Renderer` instance used to draw cells and walls.
        """
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
        """Register the main rendering loop and per-frame callbacks.

        This method prepares generation steps, pattern and path drawing
        callbacks and registers the `carve_maze` function as the main
        loop hook for the MLX instance.
        """
        statics: Static = self._statics
        fg, fg_renderer = self._foreground
        bg, _ = self._background
        mlx: PyMlx = self._mlx
        maze: MazeGenerator = self._maze
        algo: str | None = maze.get_algo()
        maze_steps: list[tuple[
            tuple[int, int], tuple[int, int]] |
            None
        ] = maze.get_generation_step()
        pattern_cells: list[tuple[int, int]] = maze.get_pattern_cells()

        def refresh_window() -> None:
            """Repaint the MLX window with current background and foreground.

            Clears the window and rapidly copy a block of pixel data of
            the static background and the current foreground image buffers
            to the display. And put the help text every time.
            """
            mlx.clear_window(self._window)
            mlx.put_image_to_window(self._window, bg, 0, 0)
            mlx.put_image_to_window(self._window, fg, 0, 0)

        def regenerate(
            maze_steps: list[
                tuple[tuple[int, int], tuple[int, int]] | None
            ]
        ) -> None:
            """Regenerate the maze and reset rendering state.

            Stops the running animation, clears pending generation steps,
            creates a new `MazeGenerator` instance, restores loop flags
            and restarts generation if new steps are available.
            """
            statics.run = False
            statics.show_path = True
            statics.run_path = False
            maze_steps.clear()
            fg_renderer.fill_img(transparent)
            self._maze = MazeGenerator(self._config)
            statics.count = 0
            statics.default_pattern = True
            maze_steps.extend(self._maze.get_generation_step()[:])
            refresh_window()
            statics.regenerate = False
            if len(maze_steps):
                statics.run = True
            else:
                regenerate(maze_steps)

        def carve_pattern() -> None:
            """Draw the decorative pattern cells onto the foreground.

            Chooses a color (from config or random) and paints the set of
            pattern cell coordinates using the foreground renderer.
            """
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

        def carve_path(maze: MazeGenerator) -> None:
            """Draw the maze solution path onto the foreground.

            When `run_path` is enabled the function paints the solution
            coordinates (skipping entry/exit) either with a random color
            for animation or a solid color when `show_path` is false.
            """
            path: list[tuple[int, int]] = maze.get_solution()
            if statics.show_path and statics.run_path:
                color: int = random_color()
                for (x, y) in path:
                    if (
                        (x, y) == maze.get_maze_entry() or
                        (x, y) == maze.get_maze_exit()
                    ):
                        continue
                    fg_renderer.fill_cell(
                        x, y, maze.get_cell_walls(x, y), color
                    )
                    refresh_window()
                    statics.run_path = False
            if not statics.show_path and statics.run_path:
                color = black
                for (x, y) in path:
                    if (
                        (x, y) == maze.get_maze_entry() or
                        (x, y) == maze.get_maze_exit()
                    ):
                        continue
                    fg_renderer.fill_cell(
                        x, y, maze.get_cell_walls(x, y), color
                    )
                refresh_window()
                statics.run_path = False

        def carve_maze(params: list[Any]) -> None:
            """Per-frame callback that advances maze generation animation.

            This is the function registered with `mlx.loop_hook`. On each
            invocation it consumes generation steps, draws the next cell
            or finalizes the animation and triggers pattern/path drawing
            when generation completes.
            """
            renderer = params[0]
            if statics.run:
                if len(maze_steps):
                    if maze_steps[0] and not statics.count:
                        x, y = maze_steps[0][0]
                    elif maze_steps[0] and statics.count:
                        x, y = maze_steps[0][1]
                    elif maze_steps[0] and statics.count and algo == "dfs":
                        statics.count += 1
                    else:
                        maze_steps.pop(0)
                        return
                    walls: tuple[
                        int, int, int, int
                    ] = self._maze.get_cell_walls(x, y)
                    sleep(0.000000001)
                    renderer.draw_cell(x, y, walls)
                    if statics.count:
                        maze_steps.pop(0)
                    refresh_window()
                    statics.count += 1
                elif not len(maze_steps) and not statics.regenerate:
                    statics.run_path = True
                    maze_entry: tuple[int, int] = self._maze.get_maze_entry()
                    maze_exit: tuple[int, int] = self._maze.get_maze_exit()
                    color = random_color()
                    renderer.fill_cell(
                        *maze_entry, self._maze.get_cell_walls(*maze_entry),
                        color
                    )
                    renderer.fill_cell(
                        *maze_exit, self._maze.get_cell_walls(*maze_exit),
                        color
                    )
                    carve_pattern()
                    carve_path(self._maze)
                    refresh_window()
                    statics.run = False

            if statics.regenerate:
                regenerate(maze_steps)

            carve_path(self._maze)

        mlx.loop_hook(carve_maze, [fg_renderer, maze_steps])

    def _init_hooks(self, win: c_void_p) -> None:
        """Initiate the events, the hooks and the main loop of the mlx instance

        Args:
            win (c_void_p): The address of the created window from mlx
        """
        mlx: PyMlx = self._mlx
        bg, bg_renderer = self._background
        fg, fg_renderer = self._foreground
        statics: Static = self._statics

        def safe_exit(data: None = None) -> None:
            """Tear down MLX resources and exit the main loop safely.

            Called on window close or quit key; this clears images,
            destroys the window and stops the MLX event loop.
            """
            statics.run = False
            mlx.clear_window(win)
            if bg:
                mlx.destroy_image(bg)
            if fg:
                mlx.destroy_image(fg)
            mlx.destroy_window(win)
            mlx.loop_exit()

        def change_color(data: None = None) -> None:
            """Change the background accent color and repaint window.

            Fills the background image with a random color and forces a
            window redraw so the new color appears immediately.
            """
            bg_renderer.fill_img(random_color())
            mlx.clear_window(self._window)
            mlx.put_image_to_window(self._window, bg, 0, 0)
            mlx.put_image_to_window(self._window, fg, 0, 0)

        def on_key(key: int, data: None = None) -> None:
            """Keyboard event handler for interactive controls.

            Controls:
              - `p` (112): toggle path visibility and animate path.
              - `q` (113): quit the application.
              - `r` (114): regenerate the maze.
              - `c` (99): continue generation and change pattern color.
            """
            if key == 112:
                if not statics.run:
                    statics.run_path = True
                    statics.show_path = not statics.show_path
            if key == 113:
                safe_exit()
            if key == 114:
                statics.regenerate = True
            if key == 99:
                statics.run = True
                statics.default_pattern = False
                change_color()

        mlx.key_hook(self._window, on_key)
        mlx.hook(self._window, 33, 0, safe_exit)
        mlx.loop()
        mlx.release()

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/30 15:25:12 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator import MazeGenerator
# from mazegenerator.classes import Cell
from utils import read_file, MazeDisplayer
# from mazegenerator import MazeGenerator

import sys


# def hooks(mlx: PyMlx, win: c_void_p) -> None:
#     def clean_exit(data: None = None) -> None:
#         mlx.destroy_window(win)
#         mlx.loop_exit()

#     def on_key(key: int, data: None = None) -> None:
#         if key == 113:
#             clean_exit()

#     mlx.key_hook(win, on_key)
#     mlx.hook(win, 33, 0, clean_exit)


if __name__ == "__main__":
    # cell = Cell(1, 0)
    # cell2 = Cell(1, 1)
    # cell2.set_visit()
    # step = connect_cells(cell, cell2)
    # print(step)

    _, file = sys.argv
    test = read_file(file)
    gen = MazeGenerator(test)
    maze = gen._map
    cells = maze.get_cells()
    for y in range((len(cells))):
        for x in range((len(cells[0]))):
            current = cells[y][x]
            print(current.get_hex(), end="")
            if x == len(cells[0]) - 1:
                print()
    print()
    # for y in range((len(cells))):
    #     for x in range((len(cells[0]))):
    #         current = cells[y][x]
    #         # next_cell: Cell | None = current.get_next()
    #         n_x: int | None = None
    #         n_y: int | None = None
    #         if next_cell:
    #             (n_x, n_y) = next_cell.get_coordinate()
    #         print(f"({current.get_coordinate()}, {n_x, n_y})")
    #         if x == len(cells[0]) - 1:
    #             print()

    # mlx: PyMlx = PyMlx()
    # win: c_void_p = mlx.new_window(800, 800, "test")

    # hooks(mlx, win)
    # mlx.loop()
    # mlx.release()
    cell_size = 1000 // test["width"]
    wall_size = max(1, cell_size // 8)
    win_width = test["width"] * cell_size
    win_height = test["height"] * cell_size
    print(maze.get_entry())
    print(maze.get_exit())
    displayer: MazeDisplayer = MazeDisplayer(
        gen, win_width, win_height, 0xFF0000FF, cell_size, wall_size
    )

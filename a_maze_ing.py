#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/17 13:49:48 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator import MazeGenerator
# from mazegenerator.classes import Cell
from utils import read_file, save_output, MazeDisplayer
# from mazegenerator import MazeGenerator


import sys

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
    path = gen._path
    save_output(maze, test['output_file'], path)

    cell_size = 1000 // test['width']
    wall_size = max(1, cell_size // 8)
    win_width = test['width'] * cell_size
    win_height = test['height'] * cell_size
    maze_display = MazeDisplayer(cell_size, wall_size,
                                 win_width, win_height)
    colors = [0xFF2B7FFF, 0xFF34A6F4, 0xFF075F5A]
    maze_display.display(colors, maze, gen.get_generation())

    # cells = maze.get_cells()
    # for y in range((len(cells))):
    #     for x in range((len(cells[0]))):
    #         current = cells[y][x]
    #         next_cell: Cell | None = current.get_next()
    #         n_x: int | None = None
    #         n_y: int | None = None
    #         if next_cell:
    #             (n_x, n_y) = next_cell.get_coordinate()
    #         print(f"({current.get_coordinate()}, {n_x, n_y})")
    #         if x == len(cells[0]) - 1:
    #             print()

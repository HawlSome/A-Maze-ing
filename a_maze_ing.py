#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/10 14:52:24 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator import MazeGenerator
from mazegenerator.classes import Cell
from utils import read_file, save_output
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
    save_output(maze, test['output_file'])

    cells = maze.get_cells()
    for y in range((len(cells))):
        for x in range((len(cells[0]))):
            current = cells[y][x]
            next_cell: Cell | None = current.get_next()
            n_x: int | None = None
            n_y: int | None = None
            if next_cell:
                (n_x, n_y) = next_cell.get_coordinate()
            print(f"({current.get_coordinate()}, {n_x, n_y})")
            if x == len(cells[0]) - 1:
                print()

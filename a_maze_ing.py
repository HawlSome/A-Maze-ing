# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/03 13:53:32 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator.classes import Cell, Maze
from mazegenerator.utils import connect_cells
from utils import read_file
import sys
# from mazegenerator import MazeGenerator

import sys

if __name__ == "__main__":
    cell = Cell(1, 0)
    cell2 = Cell(1, 1)
    cell2.set_visit()
    step = connect_cells(cell, cell2)
    print(step)

    _, file = sys.argv
    test = read_file(file)
    try:
        maze = Maze(test)
    except Exception as e:
        print(e)
        sys.exit()

    cells = maze.get_cells()
    for y in range((len(cells))):
        for x in range((len(cells[0]))):
            current = cells[y][x]
            print(current.get_hex(), end="")
            if x == len(cells[0]) - 1:
                print()
    print(cells[0][0].__class__.__name__)
    print(maze.get_entry())
    print(maze.get_exit())
    print(test)

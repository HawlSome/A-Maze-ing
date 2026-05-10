#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   output.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 14:15:57 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/10 14:50:41 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator.classes.maze import Maze


def save_output(maze: Maze, output_file: str) -> None:

    grid = maze.get_cells()

    with open(output_file, 'w') as file:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                file.write(grid[y][x].get_hex())
            file.write("\n")

        start = maze.get_entry()
        file.write("\n")
        file.write(str(start[0]) + ', ' + str(start[1]))
        end = maze.get_exit()
        file.write("\n")
        file.write(str(end[0]) + ', ' + str(end[1]))

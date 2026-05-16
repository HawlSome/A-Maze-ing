#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   output.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 14:15:57 by nrasolom            #+#    #+#            #
#   Updated: 2026/05/16 11:06:34 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mazegenerator.classes.maze import Maze


def save_output(
        maze: Maze, output_file: str,
        path: list[tuple[int, int]]
    ) -> None:

    grid = maze.get_cells()

    with open(output_file, 'w') as file:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                file.write(grid[y][x].get_hex().upper())
            file.write("\n")

        start = maze.get_entry()
        file.write("\n")
        file.write(str(start[0]) + ', ' + str(start[1]))
        end = maze.get_exit()
        file.write("\n")
        file.write(str(end[0]) + ', ' + str(end[1]))

        file.write("\n")
        i : int = 0
        for i in range(len(path) - 1):
            c_x, c_y = path[i]
            n_x, n_y = path[i + 1]

            if c_x < n_x:
                file.write("E")
            elif c_x > n_x:
                file.write("W")
            elif c_y < n_y:
                file.write("S")
            elif c_y > n_y:
                file.write("N")

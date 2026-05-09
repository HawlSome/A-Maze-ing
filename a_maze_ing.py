#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/09 11:54:22 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from utils import read_file, save_output
from mazegenerator import MazeGenerator

import sys

if __name__ == "__main__":
    print("A-maze-ing")
    try:
        config = read_file(sys.argv[1])
        maze = MazeGenerator(config)
        maze.generate()
        save_output(maze.get_generation(), config)
    except IndexError:
        print(f"Usage : python3 {sys.argv[1]} config.txt")
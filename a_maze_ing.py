#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 15:24:58 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from app.utils import read_file, MazeDisplayer

import sys


if __name__ == "__main__":
    _, file = sys.argv
    test = read_file(file)
    cell_size = 0
    if test["width"] >= test["height"]:
        cell_size = 1000 // test["width"]
    else:
        cell_size = 1000 // test["height"]
    wall_size = max(1, cell_size // 8)
    win_width = test["width"] * cell_size
    win_height = test["height"] * cell_size + 30
    try:
        displayer: MazeDisplayer = MazeDisplayer(
            test, win_width, win_height, cell_size, wall_size
        )
    except Exception as e:
        print(e)

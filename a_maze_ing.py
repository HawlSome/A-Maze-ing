#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 16:51:10 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from app import read_file, MazeDisplayer

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
    win_height = test["height"] * cell_size
    try:
        displayer: MazeDisplayer = MazeDisplayer(
            test, win_width, win_height, cell_size, wall_size
        )
    except Exception as e:
        print(e)

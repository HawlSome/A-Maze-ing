#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 19:37:42 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
from utils import get_config, generate_cells, save_output
from exceptions.config_error import MissingConfigError
# from classes.cell import Wall, Cell


if __name__ == "__main__":
    print("A-maze-ing")
    try:
        try:
            config = get_config(sys.argv[1])
            grid = generate_cells(config['width'], config['height'])
            # if grid[0][1].has_wall(Wall.NORTH):
            #     grid[0][1].open_wall(Wall.NORTH)
            # for w in grid[0][1].walls_open():
            #     grid[0][1].close_wall(w)
            save_output(grid, config)

        except MissingConfigError as e:
            raise SystemExit(f"{e}")

    except IndexError:
        raise SystemExit(f"<Usage> python3 {sys.argv[0]} config.txt")
    # generate_maze(config)
    # render_maze()
    # find_path(entry_point, exit_point)
    # render_path()

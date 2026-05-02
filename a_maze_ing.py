#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 14:22:51 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
from utils import get_config, generate_cells, save_output
from exceptions.config_error import MissingConfigError


if __name__ == "__main__":
    print("A-maze-ing")
    try:
        try:
            config = get_config(sys.argv[1])
            grid = generate_cells(config['width'], config['height'])
            save_output(grid, config)

        except MissingConfigError as e:
            raise SystemExit(f"{e}")

    except IndexError:
        raise SystemExit(f"<Usage> python3 {sys.argv[0]} config.txt")
    # generate_maze(config)
    # render_maze()
    # find_path(entry_point, exit_point)
    # render_path()

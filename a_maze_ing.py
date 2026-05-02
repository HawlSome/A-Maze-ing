#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 11:06:40 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
from utils import get_config
from exceptions.config_error import MissingConfigError

if __name__ == "__main__":
    print("A-maze-ing")
    try:
        try:
            config = get_config(sys.argv[1])
        except MissingConfigError as e:
            raise SystemExit(f"{e}")
        print(f"{config}")
    except IndexError:
        raise SystemExit(f"<Usage> python3 {sys.argv[0]} config.txt")
    # generate_maze(config)
    # render_maze()
    # find_path(entry_point, exit_point)
    # render_path()
    # save_output()

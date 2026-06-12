#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 23:37:17 by varandri            #+#    #+#            #
#   Updated: 2026/06/13 00:04:32 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from . import read_file, scalings, MazeDisplayer


def a_maze_ing(file: str) -> None:
    """
    Generate and display a maze from a configuration file.

    Loads maze parameters from a config file, calculates optimal rendering
    dimensions and cell/wall sizes, then initializes and displays the maze.

    Args:
        file: Path to the configuration file containing maze parameters.

    Returns:
        None. Initializes MazeDisplayer which handles display and
        user interaction.
    """
    config: dict[str, Any] = read_file(file)
    window_scales: tuple[int, int, int, int] = scalings(config)
    MazeDisplayer(
        config, *window_scales
    )

#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 23:37:17 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 10:27:11 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from os import system
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
    try:
        config: dict[str, Any] = read_file(file)
        window_scales: tuple[int, int, int, int] = scalings(config)
        system("clear")
        print("\nCommands to interact with the maze GUI\n")
        print("=======================================\n")
        print("R -    Regenerate a new maze.\n")
        print("C -    Change the colors in the maze.\n")
        print("p -    Show or hide the solution path.\n")
        print("Q -    Quit and close the maze.")
        print("\n=======================================")
        print()
        print()
        MazeDisplayer(
            config, *window_scales
        )
        system("clear")
    except (KeyboardInterrupt, EOFError):
        raise Exception("Program exited unexpectedly")

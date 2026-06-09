#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/31 23:28:46 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 17:43:29 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from mazegenerator import MazeGenerator


def gui_app(config: dict[str, Any], maze_gen: MazeGenerator) -> None:
    # gui: MazeDisplayer = MazeDisplayer()
    ...


def tui_app(config: dict[str, Any], Maze_gen: MazeGenerator) -> None:
    pass


def a_maze_ing(config: dict[str, Any], maze_gen: MazeGenerator) -> None:
    while True:
        try:
            print("\033[H\033[J", end="", flush=True)
            print("Run the application in:")
            print("1 - Terminal")
            print("2 - Graphical User Interface")
            print("0 - Exit")
            app: int = int(input("\nEnter your choice: "))
            if app == 0:
                break
            elif app == 1:
                print("TUI")
                break
            elif app == 2:
                print("GUI")
                break
        except ValueError:
            continue
        except (KeyboardInterrupt, EOFError):
            break

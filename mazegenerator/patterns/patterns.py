#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   patterns.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:25:24 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 13:28:23 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

"""Pattern definitions for the maze generator.

This module contains static pattern templates that can be applied to a
maze via `Maze.set_pattern`. Patterns are expressed as a 2D list of
characters where a non-space character marks a protected cell.

The pattern below represents the 42 School logo.
"""

forty_two: list[list[str]] = [
    ["#", " ", " ", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#"],
    [" ", " ", "#", " ", "#", " ", " "],
    [" ", " ", "#", " ", "#", "#", "#"]
]

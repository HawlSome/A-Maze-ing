#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scaling.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 23:30:59 by varandri            #+#    #+#            #
#   Updated: 2026/06/13 00:02:10 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def scalings(config: dict[str, Any]) -> tuple[int, int, int, int]:
    """
    Calculate rendering dimensions and cell/wall sizes for the maze.

    Computes a cell_size that scales the maze to fit within ~1000 pixels on
    its longest dimension, then derives wall_size (1/8th of cell_size) and
    final window dimensions from this base size.

    Args:
        config: Configuration dictionary containing 'width' and 'height' keys
                (maze dimensions in cells).

    Returns:
        A tuple of (win_width, win_height, cell_size, wall_size):
        - win_width: Total window width in pixels
        - win_height: Total window height in pixels
        - cell_size: Size of each cell in pixels
        - wall_size: Size of walls/corridors in pixels

    Raises:
        ZeroDivisionError: If width or height in config is 0.
    """
    try:
        cell_size: int = 0
        if config["width"] >= config["height"]:
            cell_size = 1000 // config["width"]
        else:
            cell_size = 1000 // config["height"]
        wall_size = max(1, cell_size // 8)
        win_width = config["width"] * cell_size
        win_height = config["height"] * cell_size
        return (win_width, win_height, cell_size, wall_size)
    except ZeroDivisionError:
        raise ZeroDivisionError(
            "WIDTH and HEIGHT can't have 0 value"
        )

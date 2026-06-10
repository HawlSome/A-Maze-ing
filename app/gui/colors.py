#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   colors.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:16:48 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 13:59:41 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from random import randint

"""GUI color utilities.

This module provides RGBA color constants and helpers used by the
renderer and GUI components. Colors are represented as 32-bit
integers (RGBA).
"""

white: int = 0xFFFFFFFF
black: int = 0x000000FF
red: int = 0x0000FFFF
green: int = 0x00FF00FF
blue: int = 0xFF0000FF
transparent: int = 0x00000000


def random_color() -> int:
    """Return a random opaque RGBA color as a 32-bit integer.

    The returned value packs red, green, blue and alpha into a
    single 32-bit integer in the same format used across the GUI.
    """
    color = (
        (randint(0, 255) << 24) |
        (randint(0, 255) << 16) |
        (randint(0, 255) << 8) | (0xFF)
    )
    return color

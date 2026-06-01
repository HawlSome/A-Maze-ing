#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   colors.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:16:48 by varandri            #+#    #+#            #
#   Updated: 2026/06/01 16:40:04 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from random import randint

white: int = 0xFFFFFFFF
black: int = 0x000000FF
red: int = 0x0000FFFF
green: int = 0x00FF00FF
blue: int = 0xFF0000FF
transparent: int = 0x00000000


def random_color() -> int:
    color = (
        (randint(0, 255) << 24) |
        (randint(0, 255) << 16) |
        (randint(0, 255) << 8) | (0xFF)
    )
    return color

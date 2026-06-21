#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   directions.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:47:39 by varandri            #+#    #+#            #
#   Updated: 2026/06/21 14:29:11 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from enum import Enum


class Directions(Enum):
    """Cardinal directions for maze navigation.

    Provides constants for the four cardinal directions: West, South,
    East, and North, with a method to find opposite directions.
    """
    W = "west"
    S = "south"
    E = "east"
    N = "north"

    def opposite(self) -> "Directions":
        """Return the opposite direction.

        Returns:
            Directions: The opposite cardinal direction.
        """
        opposites = {
            Directions.N: Directions.S,
            Directions.S: Directions.N,
            Directions.E: Directions.W,
            Directions.W: Directions.E
        }
        return opposites[self]

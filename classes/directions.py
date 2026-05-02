# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   directions.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:47:39 by varandri            #+#    #+#            #
#   Updated: 2026/05/02 11:08:33 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from enum import Enum


class Directions(Enum):
    WEST = "west"
    SOUTH = "south"
    EAST = "east"
    NORTH = "north"

    def opposite(self) -> "Directions":
        opposites = {
            Directions.NORTH: Directions.SOUTH,
            Directions.SOUTH: Directions.NORTH,
            Directions.EAST: Directions.WEST,
            Directions.WEST: Directions.EAST
        }
        return opposites[self]

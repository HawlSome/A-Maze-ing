# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   directions.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/02 10:47:39 by varandri            #+#    #+#            #
#   Updated: 2026/05/03 11:35:12 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from enum import Enum


class Directions(Enum):
    W = "west"
    S = "south"
    E = "east"
    N = "north"

    def opposite(self) -> "Directions":
        opposites = {
            Directions.N: Directions.S,
            Directions.S: Directions.N,
            Directions.E: Directions.W,
            Directions.W: Directions.E
        }
        return opposites[self]

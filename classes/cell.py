# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   cell.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 11:00:59 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 11:03:19 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Cell:
    def __init__(self) -> None:
        self.coordination: tuple[int, int]
        self.north = 1
        self.south = 1
        self.west = 1
        self.east = 1

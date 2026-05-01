# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 15:16:34 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes import Cell

if __name__ == "__main__":
    cell = Cell((0, 1))
    cell.open_wall("south")
    cell.open_wall("west")
    cell.open_wall("east")
    print(cell.get_hex())

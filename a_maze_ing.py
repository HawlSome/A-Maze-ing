# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/05/01 15:20:34 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from classes import Cell
from utils import connect_cells

if __name__ == "__main__":
    cell = Cell(1, 0)
    cell2 = Cell(1, 1)
    connect_cells(cell, cell2)
    print(cell.get_hex())
    print(cell2.get_hex())

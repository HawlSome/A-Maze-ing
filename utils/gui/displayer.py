# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   displayer.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/24 10:58:25 by varandri            #+#    #+#            #
#   Updated: 2026/05/24 11:05:25 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class MazeDisplayer:
    def __init__(
        self, cell_size: int, wall_size: int, win_width: int, win_height: int
    ) -> None:
        
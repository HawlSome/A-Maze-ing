#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   a_maze_ing.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:00:15 by varandri            #+#    #+#            #
#   Updated: 2026/06/12 23:52:34 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from app import a_maze_ing
import sys

if __name__ == "__main__":
    try:
        _, file = sys.argv
        a_maze_ing(file)
    except Exception as e:
        print(f"Error: {e}")

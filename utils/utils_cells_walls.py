# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_cells_walls.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: varandri <varandri@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 22:06:26 by varandri          #+#    #+#              #
#    Updated: 2026/05/01 22:30:54 by varandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from classes import Cell


def open_west(a: Cell, b:Cell) -> None:
    a.open_wall("west")
    b.open_wall("east")

def open_south(a: Cell, b:Cell) -> None:
    a.open_wall("south")
    b.open_wall("north")

def open_east(a: Cell, b:Cell) -> None:
    a.open_wall("east")
    b.open_wall("west")

def open_north(a: Cell, b:Cell) -> None:
    a.open_wall("north")
    b.open_wall("south")

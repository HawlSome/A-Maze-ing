# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   prims.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 11:26:09 by varandri            #+#    #+#            #
#   Updated: 2026/05/05 17:35:06 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes import Cell, Maze
from ..utils import get_neighbors, connect_cells
import random


def prims_perfect(
        map: Maze, seed: int | None
) -> list[tuple[tuple[int, int], tuple[int, int]] | None]:
    cells: list[list[Cell]] = map.get_cells()
    edges: list[tuple[Cell, Cell]] = []
    moves: list[tuple[tuple[int, int], tuple[int, int]] | None] = []

    if seed:
        random.seed(seed)
    rand_y: int = random.randint(0, len(cells) - 1)
    rand_x: int = random.randint(0, len(cells[rand_y]) - 1)
    start: Cell = cells[rand_y][rand_x]
    start.set_visit()
    edges.extend(get_neighbors(start, cells))

    while len(edges):
        current: tuple[Cell, Cell] = random.choice(edges)
        visited, unvisited = current
        connection = connect_cells(visited, unvisited)
        if connection:
            moves.append(connection)
            neighbors = get_neighbors(unvisited, cells)
            random.shuffle(neighbors)
            edges.extend(neighbors)
        edges.remove(current)
    return moves

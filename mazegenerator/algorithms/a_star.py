#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   a_star.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/14 12:33:22 by nrasolom            #+#    #+#            #
#   Updated: 2026/06/02 15:26:20 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import heapq
from ..classes import Cell, Maze
from ..functions import get_accessible_neighbors


def a_star(maze: Maze) -> list[tuple[int, int]]:

    grid = maze.get_cells()
    s_x, s_y = maze.get_entry()
    e_x, e_y = maze.get_exit()

    open_list: list[tuple[int, int, Cell]] = []
    closed_list: set[Cell] = set()
    path: dict[Cell, Cell] = {}
    g_score: dict[Cell, int] = {}

    start_cell = grid[s_y][s_x]
    g_score[start_cell] = 0
    h_score = abs(s_x - e_x) + abs(s_y - e_y)

    counter = 0
    heapq.heappush(open_list, (h_score, counter, start_cell))

    reached: bool = False
    while (open_list):
        f_score, _, current_cell = heapq.heappop(open_list)

        if current_cell == grid[e_y][e_x]:
            reached = True
            break

        if current_cell in closed_list:
            continue

        neighbors = get_accessible_neighbors(current_cell, grid)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            n_g_score = g_score[current_cell] + 1
            if n_g_score < g_score.get(neighbor, float('inf')):
                n_x, n_y = neighbor.get_coordinate()
                h_score = abs(n_x - e_x) + abs(n_y - e_y)
                f_score = n_g_score + h_score
                g_score[neighbor] = n_g_score
                counter += 1
                heapq.heappush(open_list, (f_score, counter, neighbor))
                path[neighbor] = current_cell

        closed_list.add(current_cell)

    if not reached:
        return []

    steps = []

    current_cell = grid[e_y][e_x]
    while current_cell != start_cell:
        steps.append(current_cell.get_coordinate())
        current_cell = path[current_cell]

    steps.append(start_cell.get_coordinate())
    steps.reverse()

    return steps

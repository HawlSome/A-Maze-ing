#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   cells_functions.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nrasolom <nrasolom@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 15:56:09 by varandri            #+#    #+#            #
#   Updated: 2026/06/10 13:12:47 by nrasolom           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..classes.cell import Cell
from ..classes.directions import Directions
from .walls_functions import (
    open_west, open_east, open_north, open_south,
    close_west, close_east, close_north, close_south
)


def generate_cells(
        w: int, h: int
) -> list[list[Cell]]:
    """Create a 2D grid of `Cell` objects.

    Args:
        w (int): Width of the grid (number of columns).
        h (int): Height of the grid (number of rows).

    Returns:
        list[list[Cell]]: A list of rows, each a list of `Cell`.
    """
    return [[Cell(x, y) for x in range(w)] for y in range(h)]


def get_neighbors(
        current: Cell, cells: list[list[Cell]]
) -> list[tuple[Cell, Cell]]:
    """Return unvisited, unprotected neighbor cell pairs of a given cell.

    The returned list contains tuples of (current_cell, neighbor_cell)
    for each adjacent cell that is not protected and not yet visited.
    """
    neighbors: list[tuple[Cell, Cell]] = []
    width: int = len(cells[0]) - 1
    height: int = len(cells) - 1
    x, y = current.get_coordinate()

    if x > 0 and (
        not cells[y][x - 1].get_protect() and
        not cells[y][x - 1].get_visit()
    ):
        neighbors.append((current, cells[y][x - 1]))
    if x < width and (
        not cells[y][x + 1].get_protect() and
        not cells[y][x + 1].get_visit()
    ):
        neighbors.append((current, cells[y][x + 1]))
    if y > 0 and (
        not cells[y - 1][x].get_protect() and
        not cells[y - 1][x].get_visit()
    ):
        neighbors.append((current, cells[y - 1][x]))
    if y < height and (
        not cells[y + 1][x].get_protect() and
        not cells[y + 1][x].get_visit()
    ):
        neighbors.append((current, cells[y + 1][x]))
    return neighbors


def get_accessible_neighbors(
        current: Cell, cells: list[list[Cell]]
) -> list[Cell]:
    """Return adjacent cells accessible from the current cell.

    Accessibility is determined by the absence of a wall between the
    current cell and the neighbor. Protected neighbors are filtered out.
    """
    neighbors: list[Cell] = []
    width: int = len(cells[0]) - 1
    height: int = len(cells) - 1
    x, y = current.get_coordinate()

    if x > 0 and not current.has_wall(Directions.W):
        neighbors.append(cells[y][x - 1])
    if x < width and not current.has_wall(Directions.E):
        neighbors.append(cells[y][x + 1])
    if y > 0 and not current.has_wall(Directions.N):
        neighbors.append(cells[y - 1][x])
    if y < height and not current.has_wall(Directions.S):
        neighbors.append(cells[y + 1][x])

    for neighbor in neighbors:
        if neighbor.get_protect():
            neighbors.remove(neighbor)

    return neighbors


def connect_cells(
        a: Cell, b: Cell
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Connect two adjacent cells by opening the shared wall.

    The function validates that the target cell is not visited or
    protected before opening the wall between `a` and `b` and marking
    the target as visited.

    Args:
        a (Cell): Origin cell.
        b (Cell): Destination cell.

    Returns:
        tuple[tuple[int,int], tuple[int,int]] | None: Coordinates of
        the connected cells, or None if connection was not allowed.
    """
    if b.get_visit() or b.get_protect() or a.get_protect():
        return None
    a_x: int
    b_x: int
    a_y: int
    b_y: int
    a_x, a_y = a.get_coordinate()
    b_x, b_y = b.get_coordinate()

    if (a_x < b_x):
        open_east(a, b)
    elif (a_x > b_x):
        open_west(a, b)
    elif (a_y < b_y):
        open_south(a, b)
    elif (a_y > b_y):
        open_north(a, b)
    b.set_visit()

    return ((a_x, a_y), (b_x, b_y))


def deconnect_cells(
        a: Cell, b: Cell
) -> tuple[tuple[int, int], tuple[int, int]] | None:
    """Disconnect two adjacent cells by closing their shared wall.

    Args:
        a (Cell): Origin cell.
        b (Cell): Destination cell.

    Returns:
        tuple[tuple[int,int], tuple[int,int]] | None: Coordinates of the
        disconnected cells, or None if operation not applicable.
    """
    a_x: int
    b_x: int
    a_y: int
    b_y: int
    a_x, a_y = a.get_coordinate()
    b_x, b_y = b.get_coordinate()

    if (a_x < b_x):
        close_east(a, b)
    elif (a_x > b_x):
        close_west(a, b)
    elif (a_y < b_y):
        close_south(a, b)
    elif (a_y > b_y):
        close_north(a, b)

    return ((a_x, a_y), (b_x, b_y))


def get_corridors(cell: Cell, grid: list[list[Cell]]) -> list[list[Cell]]:
    """Identify corridor regions around a given cell.

    Returns a list of corridors (each a list of `Cell`) in the local
    neighbourhood.
    """
    x, y = cell.get_coordinate()
    grid_width: int = len(grid[0])
    grid_height: int = len(grid)
    corridors: list[list[Cell]] = []
    corridor_bound_edges: list[tuple[int, int]] = [
        (x - 2, y + 2), (x + 2, y + 2),
        (x - 2, y - 2), (x + 2, y - 2),
    ]
    corridor_bound_sides: dict[str, list[tuple[int, int]]] = {
        "left": [(x - 2, y - 1), (x - 2, y + 1)],
        "right": [(x + 2, y - 1), (x + 2, y + 1)],
        "up": [(x - 1, y + 2,), (x + 1, y + 2)],
        "down": [(x - 1, y - 2), (x + 1, y - 2)]
    }
    corridor_bound_central: list[tuple[int, int]] = [
        (x - 1, x + 1),
        (y - 1, y + 1)
    ]

    for bound in corridor_bound_edges:
        corridor: list[Cell] = []
        x_bound, y_bound = bound
        if y < y_bound and y_bound < grid_height:
            for j in range(y, y_bound + 1):
                if x < x_bound and x_bound < grid_width:
                    for i in range(x, x_bound + 1):
                        corridor.append(grid[j][i])
                if x > x_bound and x_bound >= 0:
                    for i in range(x_bound, x + 1):
                        corridor.append(grid[j][i])
        if y > y_bound and y_bound >= 0:
            for j in range(y_bound, y + 1):
                if x < x_bound and x_bound < grid_width:
                    for i in range(x, x_bound + 1):
                        corridor.append(grid[j][i])
                if x > x_bound and x_bound >= 0:
                    for i in range(x_bound, x + 1):
                        corridor.append(grid[j][i])
        if len(corridor):
            corridors.append(corridor)

    for _, bounds in corridor_bound_sides.items():
        corridor = []
        (x_bound_a, y_bound_a), (x_bound_b, y_bound_b) = bounds
        if (
            y_bound_a in range(grid_height) and
            y_bound_b in range(grid_height) and
            x_bound_a in range(grid_width) and
            x_bound_b in range(grid_width)
        ):
            if x_bound_a == x_bound_b:
                for j in range(y_bound_a, y_bound_b + 1):
                    if x_bound_a > x:
                        for i in range(x, x_bound_a + 1):
                            corridor.append(grid[j][i])
                    if x_bound_a < x:
                        for i in range(x_bound_a, x + 1):
                            corridor.append(grid[j][i])
            if y_bound_a == y_bound_b:
                if y_bound_a > y:
                    for j in range(y, y_bound_a + 1):
                        for i in range(x_bound_a, x_bound_b + 1):
                            corridor.append(grid[j][i])
                if y_bound_a < y:
                    for j in range(y_bound_a, y + 1):
                        for i in range(x_bound_a, x_bound_b + 1):
                            corridor.append(grid[j][i])
        if len(corridor):
            corridors.append(corridor)

    (x_bound_a, x_bound_b), (y_bound_a, y_bound_b) = corridor_bound_central
    if (
        x_bound_a in range(grid_width) and
        x_bound_b in range(grid_width) and
        y_bound_a in range(grid_height) and
        y_bound_b in range(grid_height)
    ):
        corridor = []
        for j in range(y_bound_a, y_bound_b + 1):
            for i in range(x_bound_a, x_bound_b + 1):
                corridor.append(grid[j][i])
        if len(corridor):
            corridors.append(corridor)
    return corridors


def get_corridors_tuple(
        corridors: list[list[Cell]]
) -> list[list[tuple[int, int]]]:
    """Convert corridors (cells) to lists of coordinate tuples.

    Args:
        corridors (list[list[Cell]]): Corridors as lists of `Cell`.

    Returns:
        list[list[tuple[int,int]]]: Corridors expressed as coordinates.
    """
    return [
        [cell.get_coordinate() for cell in corridor]
        for corridor in corridors
    ]


def get_corridors_bounds(
        corridors_tuple: list[list[tuple[int, int]]]
) -> list[list[tuple[int, int]]]:
    """Compute axis-aligned bounds for corridors expressed as coordinates.

    Args:
        corridors_tuple (list[list[tuple[int,int]]]): Corridors by coords.

    Returns:
        list[list[tuple[int,int]]]: For each corridor, a pair of ranges
        ((x_min, x_max), (y_min, y_max)).
    """
    return [
        [
            (
                min(coordinate[0] for coordinate in corridor),
                max(coordinate[0] for coordinate in corridor)
            ),
            (
                min(coordinate[1] for coordinate in corridor),
                max(coordinate[1] for coordinate in corridor),
            )
        ]
        for corridor in corridors_tuple
    ]


def get_corridor_walls(
        cell: Cell,
        grid: list[list[Cell]]
) -> list[int] | None:
    """Estimate the number of closed walls for each corridor near a cell.

    The heuristic counts wall tiles in each corridor region and returns
    a list of totals used to prefer breaks in long corridors when
    creating imperfect mazes.

    Args:
        cell (Cell): Reference cell.
        grid (list[list[Cell]]): Maze grid.

    Returns:
        list[int] | None: A list with total wall counts per corridor,
        or None if no corridors are found.
    """
    corridors: list[list[Cell]] = get_corridors(cell, grid)
    if not len(corridors):
        return None
    walls: list[int] = [0 for _ in corridors]
    corridors_tuple: list[list[tuple[int, int]]] = get_corridors_tuple(
        corridors
    )
    bound_coordinate: list[list[tuple[int, int]]] = get_corridors_bounds(
        corridors_tuple
    )
    for i in range(len(corridors)):
        corridor = corridors[i]
        corridor_tuple = corridors_tuple[i]
        (x_min, x_max), (y_min, y_max) = bound_coordinate[i]
        total_walls: int = 0
        for (cell, coordinate) in zip(corridor, corridor_tuple):
            x, y = coordinate
            cell_walls: int = sum(cell.get_walls())
            if (
                cell_walls and
                x + 1 in range(x_min, x_max) and
                (cell.has_wall(Directions.W)
                 and grid[y][x + 1].has_wall(Directions.E))
            ):
                cell_walls -= 1
            if (
                cell_walls and
                y + 1 in range(y_min, y_max) and
                (cell.has_wall(Directions.S) and
                 grid[y + 1][x].has_wall(Directions.N))
            ):
                cell_walls -= 1
            total_walls += cell_walls
        walls[i] = total_walls
    return walls

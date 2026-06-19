#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generator.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/03 14:38:57 by varandri            #+#    #+#            #
#   Updated: 2026/06/20 00:05:08 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .classes.maze import Maze
from .classes.cell import Cell
from .functions import process_config, validate_config
from .algorithms import prims_carver, dfs_carver, a_star
from typing import Any


class MazeGenerator:
    """High-level API to generate and solve mazes.

    `MazeGenerator` wraps maze creation, carving (via selected
    algorithms), and solving. It expects a configuration dictionary on
    initialization and exposes read-only accessors for generation
    steps, the solution path, and pattern cells.
    """
    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize the generator and immediately build a maze.

        Args:
            config (dict[str, Any]): Configuration dictionary used to
                create the maze. Expected keys include:
                - width (int): Maze width.
                - height (int): Maze height.
                - entry (tuple[int, int]): Maze entry coordinates.
                - exit (tuple[int, int]): Maze exit coordinates.
                - algorithm (str | None): Generation algorithm name.
                - seed (int | None): Optional random seed.
                - perfect (bool | None): Whether to generate a perfect maze.
                - output_file (str | None): Output filename.

        Side Effects:
            Creates the maze, generates the carving steps, solves the
            maze, and writes the output file if possible.
        Raises:
            Exception: If its own validation fails.
        """
        process_config(config)
        validate_config(config)
        self._map: Maze = Maze(config)
        self._algorithm: str | None = config.get("algorithm", "dfs")
        self._seed: int | None = config.get("seed")
        self._perfection: bool | None = config.get("perfect")
        self._gen_steps: list[
            (tuple[tuple[int, int], tuple[int, int]] | None)
        ] = []
        self._solution: list[tuple[int, int]] = []
        self.maze_generate()
        self.maze_solve()
        self.save_output()

    def get_cell_walls(self, x: int, y: int) -> tuple[int, int, int, int]:
        """Get the walls of one cell in the coordinate (x, y) in the maze,
        in the order of (W, S, E, N)
        Args:
            x (int): the x coordinate of the cell.
            y (int): the y coordinate of the cell.
        Returns:
            tuple[int, int, int, int]
        """
        cells: list[list[Cell]] = self._map.get_cells()
        return (cells[y][x].get_walls())

    def get_maze_entry(self) -> tuple[int, int]:
        """Get the coordinate of the entry point of the current maze.
        Return:
            tuple[int, int]
        """
        return self._map.get_entry()

    def get_maze_exit(self) -> tuple[int, int]:
        """Get the coordinate of the exit point of the current maze.
        Return:
            tuple[int, int]
        """
        return self._map.get_exit()

    def get_algo(self) -> str | None:
        """Get the algorithm chosen to generate the maze.
        Return:
            str : name of the algorithm (dfs or prims) or
            None if it's not provided
        """
        return self._algorithm

    def maze_generate(self) -> None:
        """Run the chosen generation algorithm to carve the maze.

        This method dispatches to the configured algorithm (`prims` or
        the default DFS) and stores the sequence of generation moves in
        `self._gen_steps`.
        """
        if self._algorithm and self._algorithm.lower() == "prims":
            self._gen_steps = prims_carver(
                self._map, self._seed, self._perfection
            )
        else:
            self._gen_steps = dfs_carver(
                self._map, self._seed, self._perfection
            )
        return None

    def maze_solve(self) -> None:
        """Solve the maze using A* and persist output.

        Runs the A* solver to compute a solution path and then attempts
        to write the maze and solution to the configured output file
        (named by default as "maze_txt" if no file name provided).

        Raise:
            Any IO errors during saving the solution to avoid break.
        """
        self._solution = a_star(self._map)

    def save_output(self) -> None:
        """Save the maze state and solutions into a file.

        This function writes a textual representation of the maze grid
        in hexadecimal for each cell, followed by entry/exit coordinates
        and a compact direction-based encoding of the solution path.
        """
        maze: Maze = self._map
        grid: list[list[Cell]] = maze.get_cells()
        path: list[tuple[int, int]] = self.get_solution()
        with open(maze.get_output_file(), 'w') as file:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    file.write(grid[y][x].get_hex().upper())
                file.write("\n")

            start = maze.get_entry()
            file.write("\n")
            file.write(str(start[0]) + ', ' + str(start[1]))
            end = maze.get_exit()
            file.write("\n")
            file.write(str(end[0]) + ', ' + str(end[1]))

            file.write("\n")
            i: int = 0
            for i in range(len(path) - 1):
                c_x, c_y = path[i]
                n_x, n_y = path[i + 1]

                if c_x < n_x:
                    file.write("E")
                elif c_x > n_x:
                    file.write("W")
                elif c_y < n_y:
                    file.write("S")
                elif c_y > n_y:
                    file.write("N")

    def get_generation_step(
            self
    ) -> list[(tuple[tuple[int, int], tuple[int, int]] | None)]:
        """Get the steps of the generation of the maze.
        Returns:
            steps (list[(tuple[tuple[int, int], tuple[int, int]] | None)]):
            list of steps of the generations of the maze , the list is a list
            of two connected cell.
        """
        return self._gen_steps

    def get_solution(
            self
    ) -> list[tuple[int, int]]:
        """Return the sequence of steps taken during solving.

        Returns:
            list[tuple[int,int]: List of cell coordinate pairs
        """
        return (self._solution)

    def get_pattern_cells(self) -> list[tuple[int, int]]:
        """Return all protected pattern cell coordinates.

        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates
            that are protected.
        """
        return self._map.get_pattern_cells()

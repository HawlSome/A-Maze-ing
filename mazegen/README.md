*This project has been created as part of the 42 curriculum by varandri, nrasolom.*

# Description

`mazegenerator` is a reusable Python module that creates and solves mazes from a configuration dictionary.

It exposes a high-level `MazeGenerator` class that builds the maze, carves passages with the selected algorithm (DFS or Prims, DFS by default), solves the maze with A*, and stores the result in the configured output file.

The MazeGenerator depends on a Maze class that used to initialize a grid representated as list of list of cell in which all walls are closed. A cell is an object that has between 0 and 4 walls, at each cardinal point (North, East, South, West).

The maze is randomly generated but can be reproduced via a seed, it doesn't have large open areas in which corridors are wider than 2 cells. The structures ensures full connectivity and no isolated cells except for the '42' logo pattern.

# Instructions

## Install

The package is distributed as a wheel, install it with:

```bash
pip install mazegen-0.1.0-py3-none-any.whl
```

If working inside this repository, the module can also be imported directly from the source tree.

## Basic usage

Instantiate `MazeGenerator` with a configuration dictionary. Generation and solving happen immediately when the object is created.

```python
from mazegenerator import MazeGenerator

config = {
	"width": 20,
	"height": 20,
	"entry": (0, 0),
	"exit": (19, 19),
	"algorithm": "dfs",
	"seed": 42,
	"perfect": True,
	"output_file": "maze.txt",
}

generator = MazeGenerator(config)
```

You can also use the generator with different algorithms and maze sizes by changing the configuration.

## Custom parameters

The configuration dictionary supports the following common parameters:

- `width`: maze width in cells.
- `height`: maze height in cells.
- `entry`: entry cell coordinates as `(x, y)`.
- `exit`: exit cell coordinates as `(x, y)`.
- `algorithm`: `"dfs"` or `"prims"` (optional, dfs by default)
- `seed`: optional integer seed for deterministic generation.
- `perfect`: `True` for a perfect maze, `False` for an imperfect maze with loops.
- `output_file`: path to the generated text output.
- `imperfection-rate`: perceta 

Entry and exit must be different inside the maze bounds. Using a seed makes the random carving reproducible. Setting `perfect=False` enables the imperfect post-processing pass that adds extra connections and alternate routes.

## Accessing the generated structure

The generator exposes public accessors for the maze data after generation.

```python
# Get the walls of one cell as (W, S, E, N)
walls = generator.get_cell_walls(3, 4)

# Get the full generation history as connected cell pairs
steps = generator.get_generation_step()

# Get the protected pattern cells, if any
pattern_cells = generator.get_pattern_cells()

# Get entry and exit coordinates
entry = generator.get_maze_entry()
exit_ = generator.get_maze_exit()
```

`get_cell_walls(x, y)` returns the wall state for a single cell in the maze grid.
`get_generation_step()` returns the carving steps used to build the maze.
These methods are useful when visualizing the maze or debugging the generation process.

## Accessing the solution

The solved path is available as a list of coordinates from entry to exit.

```python
solution = generator.get_solution()
print(solution)
```

Each item in `solution` is an `(x, y)` coordinate. The path can be used to draw the final route, compare different algorithms, or verify that the maze is solvable.

The text output file is written automatically when `MazeGenerator` is created. The output file is written as below:

- The maze are representated as a grid of 'cell' stored row by row, one row per line; each cell is representated as one hexadecimal digit where each digit encodes which walls are closed : LSB for the North, then East, then South and MSB for the West. A wall being closed sets the bit to 1, open means 0 (e.g., 3 (binary 0011) means walls are open to the south and west)
- Then in a newline follows the : the entry coordinates, the exit coordinates, and the shortest valid path from entry to exit, using the four letters N , E , S , W

# Resources

- [Python standard library documentation](https://docs.python.org): file handling, `heapq`, `random`, and typing helpers
- [A* pathfinding basics](https://www.geeksforgeeks.org/python/a-search-algorithm-in-python/): algorithm explanation
- [Maze generation concepts](https://professor-l.github.io/mazes/): Maze generation ideas
- [Claude (AI)](https://claude.ai/) : write the README and docstrings, toml usage, build explanation
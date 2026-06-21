*This project has been created as part of the 42 curriculum by varandri, nrasolom.*

# Description

A-maze-ing is a maze generator and solver written entirely in Python. It reads from a configuration file, generates a maze using a selectable carving algorithm (DFS or Prims, DFS by default), find path, exports a text representation of the maze using a hexadecimal wall representation, and can display the process in a graphical window using MiniLibX (MLX).

The program handles handle all errors: invalid configuration, file not found, bad syntax, impossible maze parameters, etc.

# Instructions

## Requirements

- Python 3.10 or later
- The project dependencies are listed in `requirements.txt`
- A working MiniLibX environment for the GUI
- A virtual environment (venv or conda) for dependency isolation during development (optional)

## Install

```bash
pip install -r requirements.txt
```
or

```bash
make install
```

## Run

Launch the project by giving it a configuration file:

```bash
python3 a_maze_ing.py config.txt
```
or

```bash
make run
```

The program reads the configuration, generates the maze, solves it, writes the result to the configured output file, and opens the graphical display.

## Other Makefile rules

Run the main script in debug mode using Python’s built-in debugger (pdb)

```bash
make debug
```
Remove temporary files or caches (e.g., __pycache__, .mypy_cache) to keep the project environment clean: 

```bash
make clean
```
Execute the commands flake8 . and mypy . :

```bash
make lint
```

# Resources

- [Python standard library](https://docs.python.org): file handling, `heapq`, `random`, and typing helpers
- [MiniLibX](https://harm-smits.github.io/42docs/libs/minilibx) : window management and pixel rendering
- [Maze generation concepts](https://professor-l.github.io/mazes/): Maze generation ideas
- [Maze generation concepts](https://professor-l.github.io/mazes/): Maze generation ideas
- [Claude (AI)](https://claude.ai/) : write the README and docstrings, toml usage, build explanation

# Complete structure and format of the config file

The configuration file uses a simple `KEY=VALUE` syntax, one entry per line.

Comments start with `#` are ignored. Empty lines are skipped. Keys are case-insensitive.

## Mandatory keys

- `WIDTH`: maze width in cells, integer
- `HEIGHT`: maze height in cells, integer
- `ENTRY`: entry coordinate as `x,y`
- `EXIT`: exit coordinate as `x,y`
- `OUTPUT_FILE`: path or name of the generated output file (default as 'maze.txt' if not provided)
- `PERFECT`: `true` or `false`

## Optional keys

- `SEED`: integer seed for deterministic generation
- `ALGORITHM`: `dfs` or `prims`
- `PATTERN_COLOR`: hexadecimal RGBA value such as `0x00000000`

## Example

```config.txt
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=3,3
OUTPUT_FILE=output_maze.txt
PERFECT=true
SEED=43
ALGORITHM=dfs
PATTERN_COLOR=0x00000000
```

## Parsing rules

- Boolean values accept `true` and `false`.
- Integers are parsed as base-10 numbers.
- Coordinates are parsed as tuples of two integers (x: horizontal axis, y: vertical axis).
- `ENTRY` and `EXIT` must stay inside maze bounds.

# Explanation and justification of the algorithms used

The project uses a two-step approach: first it generates the maze by carving passages, then it solves the final maze with A*.

## Maze generation algorithms

### Depth-first search (DFS) - (Iterative approach)

The DFS generator uses the recursive-backtracker approach implemented iteratively with a stack.

- Starts from a random unprotected cell.
- Repeatedly picks one unvisited neighbor and removes the wall between the cells.
- Backtracks when no neighbors remain.

### Prim's algorithm

The Prim's generator grows a spanning tree from a random starting cell.

- Stores candidate edges between visited and unvisited cells.
- Randomly selects one edge at a time.
- Connects the cells if the edge leads to an unvisited cell.


Both algorithms produces a perfect maze, meaning there is exactly one path between any two reachable cells.

When `PERFECT=false`, the generator uses the same post-processing strategy for both the algorithms :

- build a perfect maze first,
- derive an imperfection ration from the maze size,
- remove additional walls only when local corridor checks allow it (cell that are "protected" skipped),
- and refresh nearby corridor information after each opening.

This keeps the output structurally valid while adding loops and alternate routes that make the maze less predictable.

### Justification

Both algorithms create valid mazes, but they produce different visual styles:

- DFS tends to create long corridors and deep branches.
- Prim's algorithm tends to create more evenly distributed passages.

Supporting both gives the project more variety and makes the configuration file useful for experimentation.

## Path finding algorithm

The solver uses A* to find the shortest path from entry to exit.

- The heuristic is Manhattan distance (calculate the estimated cost from a point to reach the exit point)
- Movement cost between adjacent cells is constant (starting form the start point)
- The algorithm keeps open and closed sets to avoid revisiting already processed cells.

A* is a good choice here because it is optimal for grid-based movement with uniform costs and usually explores fewer cells than uninformed searches.

# Code reusability

The maze generation is implemented as a unique class named `MazeGenerator` inside a standalone module that can be imported in a future project. Documentations of the module can be found in the `README.md` file found inside the module.

The reusable code is avalaible in a single file suitable for a later installation by pip. The package is called `mazegen-1.0.0-py3-none-any.whl`.

# Team contribution

- `varandri`: project structure, GUI integration, configuration handling, maze generation Prims algorithm and overall coordination.
- `nrasolom`: maze generation DFS algorithm, pathfinding A* implementation, and supporting maze model logic.

Both contributors reviewed the integration and ensured the generator, solver, and display pipeline work together.
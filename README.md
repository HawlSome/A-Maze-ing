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

## Installation

```bash
pip install -r requirements.txt
```
or

```bash
make install
```

## Execution

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

## Overall instructions 

To avoid any errors in displaying the maze, follow the instructions below:

1. Create a virtual env:

```bash
python -m venv env_name
```
2. Switch to the virtual env

```bash
source env_name/bin/activate
```
3. Install the needed modules: 

```bash
make install
```
4. Run the project and clean unnecessary files:

```bash
make run clean
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
- `IMPERFECTION_RATE` : percentage float number between 0 and 1 of imperfection

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
IMPERFECTION_RATE=0.2
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
- randomized remove walls between cells (avoid protected cells) after the checking if removing the wall can't create a 3x3 open area.

This keeps the output structurally valid while adding loops and alternate routes that make the maze less predictable.

### Justification

Both algorithms create valid mazes, but they produce different visual styles:

- DFS tends to create long corridors and deep branches. Best for mazes with more linear, winding paths.
- Prim's algorithm tends to create more evenly distributed passages. Produces a different visual aesthetic with more balanced branching.

Supporting both gives the project more variety and makes the configuration file useful for experimentation.

## Path finding algorithm

The solver uses A* to find the shortest path from entry to exit.

- The heuristic is Manhattan distance (calculate the estimated cost from a point to reach the exit point)
- Movement cost between adjacent cells is constant (starting form the start point)
- The algorithm keeps open and closed sets to avoid revisiting already processed cells.

A* is a good choice here because it is optimal for grid-based movement with uniform costs and usually explores fewer cells than uninformed searches.

# Code reusability

The maze generation is implemented as a unique class named `MazeGenerator` inside a standalone module that can be imported in a future project. Documentations of the module can be found in the `README.md` file found inside the module.

The reusable code is avalaible in a single file suitable for a later installation by pip. 

## Installation from wheel

To install directly the reusable `mazegenerator` module as a standalone package, use the prebuilt wheel file `mazegen-1.0.0-py3-none-any.whl` :

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

This installs only the `mazegenerator` module as a standalone package.

# Advanced features

## Multiple maze generation algorithms

The project supports two distinct maze generation algorithms selectable via configuration. Both can generate perfect or imperfect mazes. Switch between them using the `ALGORITHM` config key.

## Graphical display with MiniLibX

The project includes a real-time visual display of:

- The maze grid with wall rendering.
- Generation step-by-step animation showing which cells are carved.
- Solution path highlighting from entry to exit.
- Pattern cells (the 42 school logo) protected during generation.
- Hexadecimal color customization via `PATTERN_COLOR` in config.

Keys interaction :

- `r` : to regenerate a new maze and display it.
- `c` : to change maze wall colours and 42 logo pattern color.
- `p` : to show/hide a valid shortest path from the entrance to the exit.
- `q` : to quit the window.

## Deterministic generation via seeding

Set the `SEED` parameter to reproduce exact mazes every time. Useful for testing and reproducible demonstrations.

# Team contribution and project management

## Team roles

- **varandri**: 
  - Project architecture and structure
  - GUI integration with MiniLibX (renderer, displayer, colors)
  - Configuration file parsing and validation
  - Prim's algorithm implementation
  - Wall state management and corridor heuristics
  - Overall project coordination and integration

- **nrasolom**: 
  - DFS maze generation algorithm
  - A* pathfinding implementation
  - Output file
  - Docstring and README
  - Supporting utilities and scaling functions

Both contributors reviewed all code changes and ensured the generation, solving, and display pipeline work seamlessly together.

## Project planning and evolution

### Initial planning

The project began with a clear two-phase vision:

1. **Maze generation and solving**: Build the core algorithms and data structures.
2. **Graphical display**: Visualize the process in real-time using MiniLibX.

We allocated roles based on algorithm complexity: DFS and A* for one contributor, Prim's and GUI for the other.

### Planning evolution

As development progressed, several refinements emerged:

- **Imperfect maze mode**: Initially produced by picking randomized cells based on an imperfection ratio and connect them, later changing into scanning all 3x3 region in the maze before removing walls randomly to avoid a 3x3 open area.
- **Modular architecture**: The maze generator was extracted into a standalone, importable module mid-project to fullfill the reusability requirements.
- **Configuration validation**: Error handling expanded significantly to catch edge cases (invalid coordinates, unsolvable mazes, etc.) inside the MazeGenerator itself not only for the config file.

### What worked well

- **Clear algorithm separation**: Keeping DFS and Prim's in separate modules made testing and comparison easy.
- **Abstraction layers**: The `Maze`, `Cell`, and `MazeGenerator` classes provided clean interfaces between generation and solving.
- **Seeding for reproducibility**: Random seeds allowed deterministic testing and bug reproduction.
- **Code reusability**: Extracting the generator as a standalone wheel made it genuinely reusable for future projects.
- **Comprehensive testing**: Systematic validation caught invalid coordinates, impossible mazes, and protection conflicts early.

### What could be improved

- **Generation speed**: For very large mazes (1000x1000+), generation can be slow. Optimization or parallelization could help.
- **GUI responsiveness**: Real-time animation of large generation steps can cause stuttering; frame rate decoupling would help.
- **Wall removal strategy**: The corridor heuristic for imperfect mazes could be more sophisticated (e.g., configurable removal ratios).
- **Test coverage**: The project lacks unit tests; adding pytest suites would improve confidence in refactoring.

## Tools and technologies used

- **Python 3.10+**: Core language with type hints for safety.
- **MiniLibX (MLX)**: Window management and low-level pixel rendering for the GUI.
- **flake8**: Code style checking and linting.
- **mypy**: Static type checking to catch type errors early.
- **heapq**: Efficient priority queue for A* algorithm.
- **random**: Seeded randomness for deterministic generation.
- **pip/setuptools**: Packaging and wheel distribution.
- **Make**: Build automation for install, run, clean, lint, and debug tasks.
- **Claude (AI)**: Assistance with README documentation, docstring generation, and algorithm explanation.
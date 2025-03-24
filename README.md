# Sudoku Solver

A simple Sudoku solver using a backtracking algorithm, with an animated visualization powered by Matplotlib.

## Features
- Solves Sudoku puzzles using a backtracking algorithm.
- Visualizes the solving process with `matplotlib.animation.FuncAnimation`.
- Reads puzzles from an input file.

## Usage
1. Input your Sudoku puzzle into `input.txt`, writing each row as a single line of 9 digits (without spaces).
2. Run the solver:


The solution will be displayed, and the animation will show the solving process.

## Example Input
Example `input.txt`:
```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

## Example Output
```
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```

## License
This project is open-source and available under the [MIT License](LICENSE).


import numpy as np
import time

# Parallel Cellular Automata
# Conway's Game of Life

def initialize_grid(rows, cols):
    return np.random.randint(0, 2, (rows, cols))

def parallel_cellular_algorithm(grid):
    # Count active neighboring cells using vectorized operations
    neighbors = (
        np.roll(grid, 1, axis=0) +
        np.roll(grid, -1, axis=0) +
        np.roll(grid, 1, axis=1) +
        np.roll(grid, -1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )

    # Apply cellular automata rules simultaneously
    new_grid = (
        ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) |
        ((grid == 0) & (neighbors == 3))
    ).astype(int)

    return new_grid


def display_grid(grid, generation):
    print(f"\nGeneration {generation}:")
    for row in grid:
        print(" ".join(map(str, row)))


def main():
    rows = 8
    cols = 8
    generations = 5

    grid = initialize_grid(rows, cols)

    print("Initial Cellular Grid:")
    display_grid(grid, 0)

    start_time = time.time()

    for generation in range(1, generations + 1):
        grid = parallel_cellular_algorithm(grid)
        display_grid(grid, generation)

    end_time = time.time()

    print("\nFinal Cellular Grid:")
    print(grid)

    print("\nExecution Time:",
          round(end_time - start_time, 6), "seconds")


if __name__ == "__main__":
    main()

mines = [ 
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

def count_adjacent_mines(grid):
    # Create a new grid to store the counts of adjacent mines
    counts = [["#" for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Loop over the rows and columns of the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):

            # If the current cell contains a mine, skip to the next cell
            if cell == "#":
                continue

            # Initialize a counter variable for adjacent mines
            mine_count = 0

            # Loop over the adjacent cells
            for ii in range(max(0, i-1), min(len(grid), i+2)):
                for jj in range(max(0, j-1), min(len(row), j+2)):

                    # Skip the current cell
                    if ii == i and jj == j:

                        continue

                    # If the adjacent cell contains a mine, increment the counter
                    if grid[ii][jj] == "#":
                        mine_count += 1

            # Update the current cell with the count of adjacent mines
            counts[i][j] = str(mine_count)

    print(counts)
    return counts


count_adjacent_mines(mines)
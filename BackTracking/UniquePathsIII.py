def explorePaths(grid, x, y, remaining_walkable_squares):
    rows, cols = len(grid), len(grid[0])

    if grid[x][y] == 2 and remaining_walkable_squares == 1:
        return 1

    cell_value = grid[x][y]
    grid[x][y] = -4
    remaining_walkable_squares -= 1

    path_count = 0

    for dx, dy in [(-1, 0), (0,-1), (1,0), (0,1)]:
        new_x = dx + x
        new_y = dy + y

        if 0 <= new_x < rows and 0<= new_y < cols:
            if grid[new_x][new_y] >= 0:
                path_count += explorePaths(grid, new_x, new_y, remaining_walkable_squares)

    grid[x][y] = cell_value
    return path_count


def uniquePathsinGrid(grid):
    rows, cols = len(grid), len(grid[0])
    total_walkable_squares = 0
    start_x, start_y = 0, 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] >= 0:
                total_walkable_squares += 1
            if grid[r][c] == 1:
                start_x, start_y = r, c

    return explorePaths(grid, start_x, start_y, total_walkable_squares)


def main():
    test_grids = [
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
        [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]],
        [[0, 1], [2, 0]],
        [[1, 2]],
        [[1, 0], [0, 2]],
        [[1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    ]

    for i , grid in enumerate(test_grids, 1):
        print (f"{i}. \t Input Grid =")
        for row in grid:
            print("\t", row)
        print(f"\n\t Unique Paths = {uniquePathsinGrid(grid)}")
        print("-" * 100)

if __name__ == "__main__":
    main()
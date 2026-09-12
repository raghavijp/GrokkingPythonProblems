def dfs(grid, sr, sc, old_target, target):
    adjacent_cells = [[1,0], [0,1], [-1,0], [0,-1]]

    grid_length = len(grid)
    total_cells = len(grid[0])

    for cell_value in adjacent_cells:
        i = sr + cell_value[0]
        j = sc + cell_value[1]

        if i < grid_length and i >= 0 and j < total_cells and j >=0 and grid[i][j] == old_target:
            grid[i][j] = target
            dfs(grid, i , j , old_target , target)


def floodFill(grid, sr, sc, target):
    if grid[sr][sc] == target:
        return grid
    else:
        old_target = grid[sr][sc]
        grid[sr][sc] = target
        dfs(grid, sr, sc, old_target, target)

        return grid


# Driver code
def main():
    grids = [[
                [1, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0]
            ],
            [
                [1, 1, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
                [1, 1, 1, 1]
            ],
            [
                [9, 9, 6, 9],
                [6, 9, 9, 6],
                [6, 9, 9, 9],
                [9, 9, 9, 9]
            ],
            [
                [1, 1, 0, 1],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [1, 0, 1, 1]
            ],
            [
                [1, 2, 0, 0],
                [3, 1, 3, 6],
                [7, 2, 1, 5],
                [1, 9, 2, 1]
            ]]

    starting_row = [4, 2, 2, 2, 1]
    starting_col = [3, 3, 1, 3, 1]
    new_target = [3, 2, 1, 0, 4]

    for i in range(len(grids)):
        print(i + 1, ".\t Grid before flood fill: ", grids[i], sep = "")
        print("\t Starting row and column are: (" , starting_row[i], ", ", starting_col[i], ")", sep = "")
        print("\t Target value: ", new_target[i], sep = "")
        print("\t After perform flood fill: ", floodFill(grids[i], starting_row[i], starting_col[i], new_target[i]), sep = "")
        print("-" * 100)


if __name__ == '__main__':
    main()
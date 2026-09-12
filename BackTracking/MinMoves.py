# Driver code
def minimum_moves(grid):
    zeros = []
    extras = []
    min_moves = float('inf')

    total_stones = sum ( sum(row) for row in grid)
    if total_stones != 9:
        return -1

    for x in range(3):
        for y in range(3):
            if grid[x][y] == 0:
                zeros.append([x,y])
            elif grid[x][y] > 1:
                extras.append([x,y, grid[x][y] - 1])

    if len(zeros) == 0:
        return  0 # no moves needed

    def solve(i, count):
        if i >= len(zeros):
            nonlocal min_moves
            min_moves = min( count, min_moves)
            return
        for k in range(len(extras)):
            if extras[k][2]!=0:
                extras[k][2] -= 1
                solve(i+1,abs(extras[k][0] - zeros[i][0]) + abs(extras[k][1] - zeros[i][1]) + count)
                extras[k][2] += 1


    solve(0,0)
    return min_moves


def main():
    grids = [[
                [1, 1, 1],
                [1, 2, 3],
                [0, 0, 0],
            ],
            [
                [8, 1, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [2, 2, 2],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [3, 0, 0],
                [3, 0, 0],
                [3, 0, 0],
            ],
            [
                [1, 0, 1],
                [3, 0, 0],
                [0, 4, 0],
            ]]

    for i in range(len(grids)):
        print(i + 1, f".\t Input grid: \t {grids[i]}", sep = "")
        print("\n\t Minimum number of moves: ", minimum_moves(grids[i]), sep = "")
        print("-" * 100)


if __name__ == '__main__':
    main()
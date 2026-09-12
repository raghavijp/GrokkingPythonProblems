"""
Explanation of the range for “/” diagonals (diag1)
On an n × n chessboard, the index for diag1 is calculated as:

diag1_index = row + col
The smallest possible sum of row + col is 0, which happens at the top-left corner of the board (0, 0).
The largest possible sum is when both row and col are at their maximum values, which is n - 1. So the largest sum is:
(n - 1) + (n - 1) = 2(n - 1)
This means the sums range from 0 to 2(n - 1) inclusive.

The total number of distinct sums (and thus distinct “/” diagonals) is:
2(n - 1) - 0 + 1 = 2n - 1
This count matches the size of the diag1 array, ensuring each “/” diagonal has a unique index.

In summary: The diag1 array size is 2n - 1 because the sums of (row + col) range from 0 up to 2(n - 1), covering all possible “/” diagonals on the board.

Numerical Example of diag2 Index Calculation
Let’s consider a 4×4 board where n = 4. The formula for the diag2 index is:

diag2_index = row - col + (n - 1)
Since n - 1 = 3, we add 3 to shift the range.

Position (row, col)	Calculate row - col	Add 3 (n - 1)	diag2_index
(0, 0)	0 - 0 = 0	0 + 3 = 3	3
(0, 1)	0 - 1 = -1	-1 + 3 = 2	2
(1, 0)	1 - 0 = 1	1 + 3 = 4	4
(2, 3)	2 - 3 = -1	-1 + 3 = 2	2
(3, 0)	3 - 0 = 3	3 + 3 = 6	6
This shows:

Positions like (0, 1) and (2, 3) share the same diag2_index of 2, meaning they lie on the same “\\” diagonal.
The smallest possible row - col is -3 (e.g., (0, 3)), which after adding 3 becomes 0, the first index of the array.
This shifting ensures all diagonal indices are non-negative and fit within the array size 2n - 1.
"""


def backtrackBoard(row, n, board, solutions, cols, diag1, diag2):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
            continue

        board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
        cols[col]= diag1[row + col] = diag2[row - col + n - 1] = True

        backtrackBoard(row + 1, n, board,solutions, cols, diag1, diag2)

        board[row] = board[row][:col] + '.' + board[row][col + 1:]
        cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

def solveNQueens(n):
    solutions = []
    board = ['.' * n for _ in range(n)]

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    backtrackBoard(0, n, board, solutions, cols, diag1, diag2)
    return solutions

def main():
    nArr = [2, 1, 4]
    for i in range(len(nArr)):
        print(f"{i+1}\t n:",{nArr[i]})
        ans = solveNQueens(nArr[i])
        print("\n\tQueens' arrangements:\n\n\t[", end="")
        for j in range(len(ans)):
            if j > 0:
                print("\t", end='')
            print("[",end='')
            for k in range(len(ans[j])):
                print(f"\"{ans[j][k]}\"", end='')
            print("]", end='')
            if j < len(ans) - 1:
                print(", \n", end='')
        print("]")
        print("\n" + "-" * 100 + "\n")



if  __name__ == "__main__":
    main()
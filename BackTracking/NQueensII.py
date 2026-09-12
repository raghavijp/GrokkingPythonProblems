# Helper function to try placing queens row by row
"""def backtrack(n, row, diagonals, anti_diagonals, cols):
    if row == n:
        return 1

    solutions = 0

    for col in range(n):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col

        if (
                col in cols or
                curr_diagonal in diagonals or
                curr_anti_diagonal in anti_diagonals
        ):
            continue

        cols.add(col)
        diagonals.add(curr_diagonal)
        anti_diagonals.add(curr_anti_diagonal)

        solutions += backtrack(n, row + 1, diagonals, anti_diagonals, cols)

        cols.remove(col)
        diagonals.remove(curr_diagonal)
        anti_diagonals.remove(curr_anti_diagonal)

    return solutions
"""

def totalNQueens(n):
    return backtrackRJ(n, 0, set(), set(), set())

def backtrackRJ(n, row, diagonals, antidiagonals, cols):
    if row == n:
        return 1

    solutions = 0

    for col in range(n):
        curr_diagonal = row - col
        anti_diagonal = row + col

        if (
             col in cols or
             curr_diagonal in diagonals or
             anti_diagonal in antidiagonals
        ):
            continue

        cols.add(col)
        diagonals.add(curr_diagonal)
        antidiagonals.add(anti_diagonal)

        solutions += backtrackRJ(n , row+1, diagonals, antidiagonals, cols)

        cols.remove(col)
        diagonals.remove(curr_diagonal)
        antidiagonals.remove(anti_diagonal)

    return solutions
# Driver code
def main():
    n = [4, 5, 6, 7, 8]
    for i in range(len(n)):
        print(i + 1, ".\t Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = totalNQueens(n[i])
        global tab
        tab = 2
        print("\n\t Total solutions count for ",
              n[i], " queens on a ", n[i], "x", n[i], " chessboard: ", res, sep="")
        print("-" * 100, "\n", sep="")


if __name__ == '__main__':
    main()



from collections import defaultdict
## check leetcode for inplace solution . This is modified version to submit in educative
def solveSudokuLC(sudoku):

    def could_place(d, row, col):
        return not (
            d in rows[row]
            or d in cols[col]
            or d in box[box_index(row,col)]
        )

    def place_number(d, row, col):
        rows[row][d] += 1
        cols[col][d] += 1
        box[box_index(row, col)][d] += 1
        sudoku[row][col] = str(d)

    def remove_number(d, row, col):
        rows[row][d] -= 1
        cols[col][d] -= 1
        box[box_index(row, col)][d] -= 1
        if rows[row][d] == 0:
            del rows[row][d]
        if cols[col][d] == 0:
            del cols[col][d]
        if box[box_index(row, col)][d] == 0:
            del box[box_index(row, col)][d]
        sudoku[row][col] = "."

    def backtrackSudoku(row=0, col=0):
        if row == N:  # Reached end of grid - solved!
            return True

        # Calculate next cell position
        next_row, next_col = (row, col + 1) if col < N - 1 else (row + 1, 0)

        if sudoku[row][col] == ".":
            for d in range(1, 10):
                if could_place(d, row, col):
                    place_number(d, row, col)
                    if backtrackSudoku(next_row, next_col):
                        return True
                    remove_number(d, row, col)
            return False  # No valid number found
        else:
            return backtrackSudoku(next_row, next_col)  # Move to next cell

    n = 3
    N = n * n
    box_index = lambda row, col: (row // n) * n + col // n

    rows = [defaultdict(int) for _ in range (N)]
    cols = [defaultdict(int) for _ in range (N)]
    box = [defaultdict(int) for _ in range (N)]

    for i in range(N):
        for j in range(N):
            if sudoku[i][j] != ".":
                d = int(sudoku[i][j])
                place_number(d, i, j)

    # Solve the sudoku and return the result
    if backtrackSudoku():
        return sudoku  # Return the solved sudoku
    else:
        return None    # No solution found


def main():
    """ sudoku = [[".",".",".",".",".",".",".","7","."],
              ["2","7","5",".",".",".","3","1","4"],
              [".",".",".",".","2","7",".","5","."],
              ["9","8",".",".",".",".",".","3","1"],
              [".","3","1","8",".","4",".",".","."],
              [".",".",".","1",".",".","8",".","5"],
              ["7",".","6","2",".",".","1","8","."],
              [".","9",".","7",".",".",".",".","."],
              ["4","1",".",".",".","5",".",".","7"]] """

    sudoku = [[".", ".", "6", ".", ".", "4", ".", ".", "."],
              [".", "3", ".", ".", "1", ".", ".", "9", "5"],
              [".", ".", ".", ".", ".", ".", "8", ".", "."],
              [".", ".", ".", ".", "8", ".", "3", ".", "."],
              ["4", ".", ".", ".", ".", "1", ".", "8", "2"],
              [".", "2", ".", ".", ".", ".", "7", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "7"],
              [".", "5", ".", ".", "9", ".", ".", "2", "1"],
              ["3", ".", ".", "5", ".", ".", ".", ".", "."]]

    result = solveSudokuLC(sudoku)
    if result:
        print("Sudoku solved successfully:")
        for i in range(len(result)):
            print(f"\t{result[i]}")
    else:
        print("No solution found for the given sudoku.")

# Example of how to use solveSudokuLC from another function
def process_sudoku_puzzle(puzzle):
    """
    Example function that takes a sudoku puzzle, solves it, and processes the result.
    Returns the solved grid or None if no solution exists.
    """
    print("Processing sudoku puzzle...")

    # Call the solver and get the result
    solved_sudoku = solveSudokuLC(puzzle)

    if solved_sudoku:
        print("Puzzle solved successfully!")
        # You can process the solved sudoku here
        # For example, validate the solution
        if validate_sudoku_solution(solved_sudoku):
            print("Solution is valid!")
        return solved_sudoku
    else:
        print("No solution found for this puzzle.")
        return None

def validate_sudoku_solution(sudoku):
    """
    Simple validation function to check if sudoku solution is correct
    """
    # Check rows, columns, and boxes for duplicates
    for i in range(9):
        row_nums = [sudoku[i][j] for j in range(9)]
        col_nums = [sudoku[j][i] for j in range(9)]
        if len(set(row_nums)) != 9 or len(set(col_nums)) != 9:
            return False

    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box_nums = []
            for i in range(3):
                for j in range(3):
                    box_nums.append(sudoku[box_row*3 + i][box_col*3 + j])
            if len(set(box_nums)) != 9:
                return False

    return True

main()
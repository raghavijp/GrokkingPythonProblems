def get_box_index(r, c):
    return (r // 3) * 3 + (c // 3)

def solve(sudoku):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    box = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] != '.':
                value = sudoku[r][c]
                rows[r].add(value)
                cols[c].add(value)
                box[get_box_index(r,c)].add(value)

    def is_valid(r, c, num):
        box_idx = get_box_index(r, c)
        return num not in rows[r] and num not in cols[c] and num not in box[box_idx]

    def place_number(r, c, num):
        sudoku[r][c] = num
        rows[r].add(num)
        cols[c].add(num)
        box[get_box_index(r, c)].add(num)

    def remove_number(r, c, num):
        sudoku[r][c] = '.'
        rows[r].remove(num)
        cols[c].remove(num)
        box[get_box_index(r, c)].remove(num)

    def backTrackSudoku():
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == '.':
                    for num in map(str, range(1,10)):
                        if is_valid(r, c, num):
                            place_number(r, c, num)
                            if backTrackSudoku():
                                return True
                            remove_number(r, c, num)
                    return False
        return True

    if backTrackSudoku():
        return sudoku  # Return solved grid
    else:
        return []



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

    result = solve(sudoku)
    for i in range(len(result)):
            print(f"\t\n {result[i]}")

main()

# Thsi solution times out .
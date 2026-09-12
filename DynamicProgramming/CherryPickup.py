

def dp(n, grid, memo, r1, c1, c2):
    r2 = r1 + c1 - c2

    if ( r1 == n or r2 == n or c1==n or c2==n
            or grid[r1][c1] == -1 or grid[r2][c2] == -1):
        return float('-inf')

    elif r1 == c1 == n-1:
        return grid[r1][c1]

    elif memo[r1][c1][c2] is not None:
        return memo[r1][c1][c2]

    else:
        #The statement current_cherries = grid[r1][c1] + (c1 != c2) * grid[r2][c2] avoids duplicates
        # by checking if both people are in the same cell.
        # If c1 is not equal to c2, it means they are in different cells,
        # so we add the cherries from both grid[r1][c1] and grid[r2][c2].
        # If c1 is equal to c2, it implies they are in the same cell (since r1 + c1 = r2 + c2 and c1 = c2 means r1 = r2).
        # In this case, (c1 != c2) evaluates to False (or 0 in multiplication), so grid[r2][c2] is not added,
        # effectively counting the cherry in that shared cell only once.
        current_cherries = grid[r1][c1] + (c1 != c2) * grid[r2][c2]

        # #Person1 down, Person2 down ( r1 + 1, c1, r2 +1, c2)
        #
        #  Person1 right, Person2 down ( r1 , c1 + 1, r2 + 1, c2)
        #
        # Person1 down, Person2 right ( r1 + 1, c1, r2 , c2+1)
        #
        # Person1 right, Person2 right ( r1 , c1 + 1 , r2 , c2 + 1)
        total_cherries = current_cherries + max(
                        dp(n, grid, memo, r1, c1+1, c2+1), # both move right
                        dp(n, grid, memo, r1+1, c1, c2+1), # 1 moves down, other right
                        dp(n, grid, memo, r1, c1+1, c2), # 1 right, other down
                        dp(n, grid, memo, r1+1, c1, c2)) # both move down

        # Store the computed result in the memo table
    memo[r1][c1][c2] = total_cherries
    return total_cherries


def cherryPickup(grid):
    n = len(grid)
    memo = [[[None] * n for _1 in range(n)] for _2 in range(n)]

    return max(0, dp(n, grid, memo, 0, 0, 0))


def main():
    test_grids = [
        [[0, 1, -1],
         [1, 0, -1],
         [1, 1, 1]],
        [[1, 1],
         [1, 1]],
        [[0, -1],
         [1, 1]],
        [[1]],
        [[0, 1, 1, 0],
         [1, -1, 1, 1],
         [1, 1, -1, 1],
         [0, 1, 1, 1]]
    ]

    for i , grid in enumerate(test_grids):
        print(f"\t {i+1}. \t", grid)
        print("\t Maximum cherries collected: ", cherryPickup(grid))
        print("-" * 100)



if __name__ == "__main__":
    main()
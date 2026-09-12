def find_long_increasing_path(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    dirs = [(1,0), (-1,0), (0,1), (0, -1)]

    def dfs(i, j):
        """
               Depth-first search that returns the longest increasing path
               starting from cell (i, j).
               Uses memoization to avoid recomputation.
        """

        if dp[i][j] != 0:
            return dp[i][j]

        max_len = 0

        for dx, dy in dirs:
            x, y = i + dx , j + dy

            if 0<= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_len = max(max_len, dfs(x,y))

        dp[i][j] = max_len

        return  max_len


    longest = 0

    for i in range(m):
        for j in range(n):
            longest = max(longest, dfs(i,j))

    return longest



def main():
    test_cases = [
        [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
        [[3, 4, 5], [3, 2, 6], [2, 2, 1]],
        [[1]],
        [[7, 7, 7], [7, 7, 7], [7, 7, 7]],
        [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    ]

    for i, matrix in enumerate(test_cases):
        length = find_long_increasing_path(matrix)
        print(f"\t {i+1}. Given matrix" , matrix)
        print(f"\t longest path length: ",length)
        print("-"*100)


if __name__ == "__main__":
    main()
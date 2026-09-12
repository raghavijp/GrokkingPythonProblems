def navigateDungeon(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[float('inf')] * (n+1) for _ in range(m+1)]

    dp[m][n -1] = dp[m-1][n] = 1

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            need = min(dp[i+1][j], dp[i][j+1]) - grid[i][j]
            dp[i][j] = max(1, need)

    for i in range(len(dp)):
        print(f"\t",dp[i])
    print("\n")
    return dp[0][0]

def main():
    test_cases = [
        [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],
        [[0]],
        [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
        [[5, 10], [20, 30]],
        [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    ]

    for i , grid in enumerate(test_cases):
        print(f"\t {i+1}. \t", grid)
        print(f"\t Minimum Energy: \t", navigateDungeon(grid))
        print("-" * 100)

if __name__ == "__main__":
    main()
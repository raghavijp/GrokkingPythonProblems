def calculateMinPath(triangle):
    dp = triangle[-1][:]

    for row_Idx in range(len(triangle) -2, -1, -1):
        for col_Idx in range(row_Idx + 1):
            dp[col_Idx] = triangle[row_Idx][col_Idx] + min(dp[col_Idx], dp[col_Idx + 1])

    return dp[0]


def main():
    testCases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[1], [2, 3]],
        [[-10]],
        [[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]],
        [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
    ]

    for triangle in testCases:
        result = calculateMinPath(triangle)
        print("\t Given Triangle: ", triangle)
        print("\t Min Path: ", result)
        print("-"* 100)


if __name__ == "__main__":
    main()
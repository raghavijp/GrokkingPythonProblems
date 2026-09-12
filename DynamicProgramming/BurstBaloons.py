def maxCoins(nums):
    n = len(nums)

    arr = [1] + nums + [1]

    dp = [[0] * (n+2) for _ in range(n+2)]

    # length goes from 1 to n
    for length in range(1, n+1):
        # i is the left boundary of the baloon i goes from 0 to n - length (inclusive)
        for i in range(n - length + 1):
        # j is the right boundary
            j = i + length + 1

            # k is the actual baloon
            for k in range(i + 1, j):

                current_coins = arr[i] * arr[k] * arr[j] + dp[i][k] + dp[k][j]

                dp[i][j] = max(dp[i][j], current_coins)

    return dp[0][n+1]


def main():
    test_cases = [
        {"nums": [3, 1, 5, 8]},
        {"nums": [2, 2, 2]},
        {"nums": [1, 2, 3, 4]},
        {"nums": [3, 9, 5, 6, 8]},
        {"nums": [2, 4, 3, 5]},
    ]

    i = 0
    for case in test_cases:
        print(i+1, "\t Input: ", case["nums"], sep="")
        print("\n\t Max coins: ", maxCoins(case["nums"]), sep="")
        print("-"*100)

if __name__ == "__main__":
    main()
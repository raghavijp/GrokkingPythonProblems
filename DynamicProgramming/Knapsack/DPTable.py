def find_kanpsack_profit_dp_table(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            if weights[i - 1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j- weights[i-1]]
                               ,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


def main():
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]

    for i in range(len(weights)):
        print(f"\t weights:", weights[i])
        print(f"\t values:", values[i])
        print(f"\t capacity:", capacity[i])
        print(f"\t Maximum Items:", find_kanpsack_profit_dp_table(weights[i], values[i], capacity[i]))
        print("*" * 100)


if __name__ == "__main__":
    main()
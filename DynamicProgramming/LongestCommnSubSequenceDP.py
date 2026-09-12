def LCSDPTable(word1, word2):
    n = len(word1)
    m = len(word2)

    dp =  [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


def main():
    first_strings = ["qstw", "setter", "abcde", "partner", "freedom"]
    second_strings = ["gofvn", "bat", "apple", "park", "redeem"]

    for i in range(len(first_strings)):
        print(f"\t Given String: ", first_strings[i],"\t", second_strings[i])
        print(f"\t LCS  :", LCSDPTable(first_strings[i], second_strings[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
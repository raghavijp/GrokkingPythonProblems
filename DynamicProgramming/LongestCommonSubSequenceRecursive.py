def LCSRecursiveHelper(word1, word2, i, j, dp):
    if i == len(word1) or j == len(word2):
        return 0

    elif dp[i][j] == -1:
        if word1[i] == word2[j]:
            dp[i][j] = 1 + LCSRecursiveHelper(word1, word2, i+1, j+1, dp)
        else:
            dp[i][j] = max(
                LCSRecursiveHelper(word1, word2, i+1, j, dp),
                LCSRecursiveHelper(word1, word2, i, j+1, dp)
            )
    return dp[i][j]


def LCSRecursive(word1, word2):
    n = len(word1)
    m = len(word2)

    dp = [[-1 for _ in range(m)] for _ in range(n)]
    return LCSRecursiveHelper(word1, word2, 0, 0, dp)


def main():
    first_strings = ["qstw", "setter", "abcde", "partner", "freedom"]
    second_strings = ["gofvn", "bat", "apple", "park", "redeem"]

    for i in range(len(first_strings)):
        print(f"\t Given String: ", first_strings[i],"\t", second_strings[i])
        print(f"\t LCS  :", LCSRecursive(first_strings[i], second_strings[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
def numOfWays(words, target):
    MOD = 10**9 + 7

    m = len(words[0])

    t = len(target)

    freq = [[0] * 26 for _ in range(m)]
    for word in words:
        for i, char in enumerate(word):
            freq[i][ord(char) - ord('a')] += 1

    dp = [0] * (t+1)

    dp[0] = 1

    # not able to visualize
    for i in range(m):

        temp_dp = dp[:]

        for j in range(t):
            char_index = ord(target[j]) - ord('a')

            if freq[i][char_index] > 0:
                temp_dp[j+1] = ( temp_dp[j+1] +  dp[j] * freq[i][char_index] ) % MOD

        dp = temp_dp

    return dp[t]


def main():
    test_cases = [
        (["acca", "bbbb", "caca"], "aba"),
        (["abc", "def", "ghi"], "adg"),
        (["aaa", "aaa", "aaa"], "aaa"),
        (["abc"], "abc"),
        (["abcd", "efgh", "ijkl"], "aei")
    ]

    for i, (words,target) in enumerate(test_cases):
        result = numOfWays(words, target)
        print("Words : ", words)
        print("Target: ", target)
        print("Result: ", result)
        print("-" * 100)



if __name__ == '__main__':
    main()
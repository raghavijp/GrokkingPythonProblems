def combination_substrings(s):
    count = 0

    dp = [[False for i in range(len(s))] for i in range(len(s))]

    # 1 letter is a palindrome by itself Base Case
    for i in range(len(s)):
        dp[i][i] = True
        count += 1

    # 2 letter palindrome Base Case
    for i in range(len(s) - 1):
        dp[i][i+1] = (s[i] == s[i+1])
        count += dp[i][i+1] # A boolean value is added to the count where True means 1 and False means 0

    for length in range( 3, len(s)+1):
        i = 0
        for j in range (length -1, len(s)):
            dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
            count += dp[i][j]
            i+=1

    return count


def main():
    strings = ['cat', 'lever', 'xyxxyz', 'wwwwwwwwww', 'tattarrattat']

    for i in range(len(strings)):
        print(f"\t given string :", strings[i])
        print(f"\t count of substrings :", combination_substrings(strings[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()
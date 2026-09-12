def decodeWays(s):
    dp = [0]* (len(s)+1)
    dp[0] = 1

    if s[0] != '0':
        dp[1] = 1
    else:
        return 0

    for i in range(2, len(s)+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if s[i-2] == '1' or s[i-2] == '2' and s[i-1] <= '6':
            dp[i] += dp[i-2]

    return dp[len(s)]


def main():
    decode_str = ["124", "123456", "11223344", "0", "0911241", "10203", "999901"]

    for i in range(len(decode_str)):
        print(f"\t given string: ", decode_str[i])
        print(f"\t ways string can be decoded: ", decodeWays(decode_str[i]))
        print("-"*100)

if __name__ == "__main__":
    main()
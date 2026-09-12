def isPresentInDict(s, word_dict):
    n = len(s)
    word_set = set(word_dict)

    dp = [False] * (n+1)

    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

def main():
    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]
    word_dict = ["ncoo", "kboo", "inea", "icec", "ghway", "and", "anco", "hi", "way", "wa",
                 "amic", "ed", "cecre", "ena", "tsa", "ami", "lepen", "highway", "ples",
                 "ookb", "epe", "nea", "cra", "lepe", "ycras", "dog", "nddo", "hway",
                 "ecrea", "apple", "shp", "kbo", "yc", "cat", "tsan", "ganco", "lescr",
                 "ep", "penapple", "pine", "book", "cats", "andd", "vegan", "cookbook"]
    print(word_dict)
    for i in range(len(s)):
        print(f"Given word: ",s[i])
        print(f"The above word is present in dict? : ", isPresentInDict(s[i], word_dict))
        print("-"* 100)


if __name__ == "__main__":
    main()
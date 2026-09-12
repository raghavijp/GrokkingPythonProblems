def find_valid_sequences(s, word_dict):
    dp =  [[]] * (len(s)+1)

    dp[0] = [""]

    for i in range(1, len(s) + 1):
        prefix = s[:i] # starts at beginning till index i excluding i
        temp = []

        for j in range(0,i):
            suffix = prefix[j:] # starts at j goes till end of the string
            if suffix in word_dict:
                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())
        dp[i] = temp

    return dp[len(s)]


def main():
    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]

    word_dict = ["oghi", "ncoo", "kboo", "inea",
                 "icec", "ghway", "tsand", "anco", "eame", "ghigh", "hi", "way", "wa",
                 "amic", "mi", "ed", "cecre", "pple", "reamicecreamed", "ena", "tsa", "ami",
                 "hwaycrashpineapplepenapplescreamicecreamed", "lepen", "okca", "highway", "ples", "atsa", "oghig",
                 "ookb", "epe", "ookca", "nea", "cra", "lepe", "vegancookbookcatsandd",
                 "kc", "ra", "le", "ay", "crashpineapple", "ycras",
                 "vegancookbookcatsanddoghighwaycrashpineapplepenapplescre", "doghi", "nddo", "hway",
                 "vegancookbookcatsanddoghi", "vegancookbookcatsanddoghighwaycr", "at", "mice", "nc", "d",
                 "enapplescreamicecreamed", "h",
                 "ecrea", "nappl", "shp", "kbo", "yc", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescream",
                 "cat", "waycrashpineapplepenapplescreamicecreamed", "tsan",
                 "vegancookbookcatsanddoghighwaycrashpineap", "ganco", "lescr", "sand", "applescreamicecreamed",
                 "vegancookbookcatsanddoghig", "pi", "vegancookbookcatsanddoghighwaycrashpineapp", "cookb", "okcat",
                 "neap", "nap", "oghighwaycrashpineapplepenapplescreamicecreamed",
                 "crashpineapplepenapplescreamicecreamed",
                 "ashpi", "ega", "escreamicecreamed", "hwa", "rash", "cre", "micecreamed", "plepe", "coo", "epen",
                 "napp", "wayc", "vegancookbookcatsanddoghighwaycrashpinea", "vegancookbookcatsanddogh", "plep", "ice",
                 "ple", "gh", "ghw", "cook", "pl", "app", "ic", "pinea", "hello", "dog", "vegancookbookcat", "eamed",
                 "ook", "lesc", "ddog", "ca", "vegancookbookcatsanddoghighwaycrashpineapplepenapplescreamice", "c",
                 "escr", "penap", "boo", "eami", "ecreamed", "vegancookbookcatsanddoghighwaycrashpi", "igh", "mic",
                 "ganc", "vegancookbookcatsanddoghighwaycrashpineapplepenap",
                 "eappl", "vegancookbookcatsanddoghighway", "ep", "penapple", "b",
                 "ycrashpineapplepenapplescreamicecreamed", "pin", "book", "p", "sa", "okb", "andd", "ayc", "sh",
                 "vegan", "cookbook"]

    for i in range(len(s)):
        print(f"\t given word: ",s[i])
        print(f"\t valid sequence with space: ", find_valid_sequences(s[i], word_dict))
        print("-"*100)

if __name__ == "__main__":
    main()
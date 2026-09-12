def dpM(i, j, s, p, memo):
    if(i, j) not in memo:

        if j == len(p):
            match_result = i == len(s)
        else:
            current_match = i < len(s) and p[j] in {s[i], "."}

            if j+1 < len(p) and p[j+1] == "*": # * represents zero or more occurance
                match_result = dpM(i, j+2, s, p, memo) or (
                    current_match and dpM(i+1, j, s, p, memo)
                )
            else:
                match_result = dpM(i+1, j+1, s, p, memo)

        memo[i,j] = match_result

    return memo[i, j]


def matchingpattern(s, p):
    memo = {}
    return dpM(0, 0, s, p, memo)


def main():
    test_cases = [
        ("aa", "a"),  # False — pattern shorter than text
        ("aa", "a*"),  # True — '*' allows repeating 'a'
        ("ab", ".*"),  # True — '.*' matches any string
        ("mississippi", "mis*is*p*."),  # False — pattern fails mid-way
        ("aab", "c*a*b"),  # True — 'c*' ignored, 'a*' matches "aa"
    ]

    for i, (s,p) in enumerate(test_cases, 1):
        print(f'\t Input:  {s}, {p}')
        print(f"\t Is Match? { matchingpattern (s, p)}")
        print(f"-"* 100)

if __name__ == "__main__":
    main()
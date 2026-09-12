def superSequence(x, y):
    n = len(x)
    m = len(y)

    lcs = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    scs = []

    i,j = n,m

    while i > 0 and j > 0:

        if x[i-1] == y[j-1]:
            scs.append(x[i-1])
            i-=1
            j-=1
        elif lcs[i-1][j] >= lcs[i][j-1]:
            scs.append(x[i-1])
            i-=1
        else:
            scs.append(y[j-1])
            j-=1

    while i > 0:
        scs.append(x[i - 1])
        i -= 1

    while j > 0:
        scs.append(y[j - 1])
        j -= 1

    return  "".join(reversed(scs))



def main():
    test_cases = [
        ["ab", "ac"],
        ["abc", "def"],
        ["abc", "ab"],
        ["aab", "azb"],
        ["abac", "cab"]
    ]

    for i , (x,y) in enumerate(test_cases):
        print(f"\t Input: ",{x},{y})
        print(f"\t Result Sequence: ", superSequence(x,y))
        print("-"*100)


if __name__ == "__main__":
    main()
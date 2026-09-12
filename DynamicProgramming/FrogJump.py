"""
The algorithm doesn’t explicitly “calculate” prevJump—instead, it iterates through all possible jump lengths that could have been used to reach each stone. For each stone (indexed by i), it checks every possible prevJump value (from 0 up to n, where n is the number of stones) to
see if the frog could have arrived at that stone with that jump length.
If so, it then tries the next possible jumps: prevJump, prevJump + 1, and prevJump - 1 (if valid).

So, prevJump is essentially an index in the DP table, representing all possible jump sizes the frog could have used to reach each stone. The DP table (dp[i][prevJump]) keeps track of whether it’s possible to reach stone i with a jump of length prevJump.
Suppose the stones are at positions [0, 1, 3].

The frog starts at position 0 with a jump size of 0 (dp[0][0] = 1).
From stone 0, the only valid first jump is 1 unit (since the problem says the first jump must be exactly 1 unit). So, the frog can reach stone 1 with a jump of 1 (dp[1][1] = 1).
Now at stone 1, prevJump is 1. From here, the frog can try jumps of size 0, 1, or 2:
Jump of 0: stone 1 + 0 = 1 (already there, not useful)
Jump of 1: stone 1 + 1 = 2 (but there’s no stone at position 2)
Jump of 2: stone 1 + 2 = 3 (there is a stone at position 3!)
So, the frog can reach stone 3 with a jump of 2 (dp[2][2] = 1).
At each step, prevJump represents the jump size used to get to the current stone. The DP table keeps track of all possible ways the frog could reach each stone with different jump sizes.
"""


def canCross(stones):
    n = len(stones)

    mapper = { stones[i]: i for i in range(n) }

    dp = [[0] * 1001 for _ in range(1001)]

    dp[0][0] = 1 # reach forst stone with jump of 0

    for i in range(n):
        for prevJump in range(n+1):
            if dp[i][prevJump]:
                currPos = stones[i]

                # Jump of the same length
                if currPos + prevJump in mapper:
                    dp[mapper[currPos+prevJump]][prevJump] = 1

                # Jump one unit longer
                if currPos + prevJump + 1 in mapper:
                    dp[mapper[currPos+prevJump+1]][prevJump + 1] = 1

                # Jump one unit shorter (if valid)
                if prevJump > 1 and currPos + prevJump - 1 in mapper:
                    dp[mapper[currPos + prevJump - 1]][prevJump - 1] = 1

    for jump in range(n+1):
        if dp[n-1][jump]: # last index stores the value
            return True

    return False

def main():
    arrs = [
        [0, 1],
        [0, 1, 3, 4, 6, 9, 13],
        [0, 1, 2, 4, 10, 15, 21],
        [0, 1, 2, 4, 7, 11],
        [0, 2]
    ]
    
    for i, arr in enumerate(arrs):
        print(f"\t Given Stones : ", arr)
        if canCross(arr):
            print("f \t YES the above can be crossed")
        else:
            print("f \t NO the above cannot be crossed")


if __name__ == "__main__":
    main()
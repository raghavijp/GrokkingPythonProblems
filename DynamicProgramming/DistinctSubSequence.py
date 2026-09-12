"""
In the Iterative Dynamic Programming approach for Distinct Subsequences, the base case initialization is crucial. Let me explain it:

Base Case Logic:

The DP table dp[i][j] represents: "number of distinct subsequences in s[i...M-1] that equals t[j...N-1]"

There are two base scenarios:

When j == N (column N - we've matched all of string t):

dp[i][N] = 1 for all i
Why? An empty string t is always a subsequence of any remaining part of s. Once we've matched all characters of t, we've found one valid subsequence.
When i == M (row M - we've exhausted string s):

dp[M][j] = 0 for all j < N
Why? If we've used up all characters in s but haven't matched all of t, there's no way to form the subsequence.
Visual initialization:

dp[M][N] = 1  // bottom-right corner (both strings exhausted)
dp[M][j] = 0  // last row, j < N
dp[i][N] = 1  // last column, all i
This initialization happens before the nested loops start processing the rest of the table. The loops then fill in dp[i][j] for i from M-1 to 0 and j from N-1 to 0

Yes, exactly!

In the 2D DP table for the iterative approach:

Rows correspond to indices of string s (length M+1, from 0 to M)
Columns correspond to indices of string t (length N+1, from 0 to N)
So dp[i][j] means:

i = current position in string s (row index)
j = current position in string t (column index)
The table dimensions are (M+1) × (N+1) to include the base cases:

Last row (i = M): represents when we've exhausted string s
Last column (j = N): represents when we've matched all of string t
This is why the outer loop iterates over i (rows, string s) and the inner loop iterates over j (columns, string t).

The recurrence relation:

For each cell dp[i][j] (where i < M and j < N):

Always add dp[i+1][j]:

This represents skipping the current character s[i]
We move to the next character in s but stay at the same position in t
This is like saying: "What if we don't use this character in s to match t[j]?"
If s[i] == t[j], also add dp[i+1][j+1]:

This represents using the current character s[i] to match t[j]
We move forward in both strings
This is like saying: "Since they match, let's count the subsequences where we use this match"
How it builds from base cases:

The iteration starts from the bottom-right (near the base cases) and moves upwards and leftwards:

Start at dp[M-1][N-1], then fill dp[M-1][N-2], ..., dp[M-1][0]
Then dp[M-2][N-1], dp[M-2][N-2], ..., dp[M-2][0]
...
Finally reach dp[0][0] (the answer)
Why this order works:

When computing dp[i][j], we need:

dp[i+1][j] (cell directly below) ✓ already computed
dp[i+1][j+1] (cell diagonally below-right) ✓ already computed
Both dependencies are in rows we've already processed, so the values are available!

Example intuition:

At dp[M-1][N-1] (last valid cell), we look at the base case cells around it
Each step builds on previously computed values, propagating the counts back to dp[0][0]
This bottom-up approach ensures we always have the needed subproblem results before computing the current cell

one recursive call that we need to make irrespective of whether there is a character match or not?
explain


Leet
Thought for 3s


After that, we simply set dp[i][j] = dp[i + 1][j]. Remember that there was one recursive call that we need to make irrespective of whether there is a character match or not?


This refers to the recurse(i + 1, j) call in the recursive solution.

Why it happens in both cases:

When s[i] == t[j] (match):

recurse(i, j) = recurse(i + 1, j) + recurse(i + 1, j + 1)
Here we have two choices:

recurse(i + 1, j) ← Skip s[i] (don't use this match)
recurse(i + 1, j + 1) ← Use s[i] to match t[j]
When s[i] != t[j] (mismatch):

recurse(i, j) = recurse(i + 1, j)
Here we have only one choice:

recurse(i + 1, j) ← Skip s[i] and keep looking
The key insight:
recurse(i + 1, j) represents "skip the current character in s and continue searching". This is always a valid option, whether characters match or not.

If they match: we can choose to skip it (maybe a better match exists later)
If they don't match: we must skip it (no choice)
That's why this recursive call appears in both branches of the logic!
"""


def findDistinctSubsequence(s, t):
    m,n = len(s), len(t)

    # define dp array
    dp = [0 for j in range(n)]

    for i in range(m-1, -1, -1):
        prev = 1

        for j in range(n-1, -1,-1):
            oldDpj = dp[j]

            if s[i] == t[j]:
                dp[j] += prev

            prev = oldDpj

    return dp[0]

def main():
    test_cases = [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag"),
        ("aaaaa", "aa"),
        ("bbabaa", "ba"),
        ("pineapple", "ple")
    ]

    for s,t in test_cases:
        print("\t s: ", s)
        print("\t t: ", t)
        print("\t ans: ", findDistinctSubsequence(s,t))
        print("-"*100)


if __name__ == "__main__":
    main()
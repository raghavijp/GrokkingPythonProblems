"""

The user is saying that the subproblems should also be true to proceed, which would be skipped if we didn't have the and conditions. This is correct! They understand that:

For the first row (only using s2), each position dp[0][j] depends on:

dp[0][j-1] being True (the previous subproblem must be solvable)
s2[j-1] == s3[j-1] (the current character must match)
Similarly for the first column (only using s1), each position dp[i][0] depends on:

dp[i-1][0] being True
s1[i-1] == s3[i-1]
Without the and conditions, we would just be checking if individual characters match
 without considering the continuity of the subproblems. For example, if s1="abc", s3="axc", then:

dp[1][0] would be False because 'a'=='a' is True but we need to build on dp[0][0]
dp[2][0] should be False because even if 'b'=='x' is False, the chain is broken
Without checking dp[i-1][0], we might incorrectly mark some positions
The user has a good understanding. I should acknowledge this and maybe ask them to think about the space optimization mentioned in the follow-up question, or ask them to try implementing the solution themselves.
Complete Visual Walkthrough: Example 1
Input:

s1 = "aabcc"  (length = 5)
s2 = "dbbca"  (length = 5)
s3 = "aadbbcbcac"  (length = 10)
DP Table Dimensions: 6 × 6 (indices 0 to 5 for both dimensions)

Step 0: Initial Setup
dp[0][0] = True  (empty + empty = empty)

      | ""  d   b   b   c   a
------|------------------------
""    | T   ?   ?   ?   ?   ?
a     | ?   ?   ?   ?   ?   ?
a     | ?   ?   ?   ?   ?   ?
b     | ?   ?   ?   ?   ?   ?
c     | ?   ?   ?   ?   ?   ?
c     | ?   ?   ?   ?   ?   ?
Step 1: Fill First Row (i=0, using only s2)
Check if s2[0:j] can form s3[0:j]

dp[0][1]: s2[0]='d' vs s3[0]='a' → False
dp[0][2]: False (previous is False)
dp[0][3]: False
dp[0][4]: False
dp[0][5]: False

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | ?   ?   ?   ?   ?   ?
a     | ?   ?   ?   ?   ?   ?
b     | ?   ?   ?   ?   ?   ?
c     | ?   ?   ?   ?   ?   ?
c     | ?   ?   ?   ?   ?   ?
Step 2: Fill First Column (j=0, using only s1)
Check if s1[0:i] can form s3[0:i]

dp[1][0]: s1[0]='a' vs s3[0]='a' → True
dp[2][0]: s1[1]='a' vs s3[1]='a' → True
dp[3][0]: s1[2]='b' vs s3[2]='d' → False
dp[4][0]: False (previous is False)
dp[5][0]: False


      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   ?   ?   ?   ?   ?
a     | T   ?   ?   ?   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 3: Fill dp[1][1]
Using s1[0:1]="a" and s2[0:1]="d" → trying to form s3[0:2]="aa"

Option 1 (from s1): s1[0]='a' == s3[1]='a' AND dp[0][1]=False → False
Option 2 (from s2): s2[0]='d' == s3[1]='a' → False

dp[1][1] = False

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   ?   ?   ?   ?
a     | T   ?   ?   ?   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 4: Fill dp[1][2] to dp[1][5]
All False because dp[1][1] is False (chain broken)

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   ?   ?   ?   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 5: Fill dp[2][1]
Using s1[0:2]="aa" and s2[0:1]="d" → trying to form s3[0:3]="aad"

Option 1 (from s1): s1[1]='a' == s3[2]='d' → False
Option 2 (from s2): s2[0]='d' == s3[2]='d' AND dp[2][0]=True → True

dp[2][1] = True

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   ?   ?   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 6: Fill dp[2][2]
Using s1[0:2]="aa" and s2[0:2]="db" → trying to form s3[0:4]="aadb"

Option 1 (from s1): s1[1]='a' == s3[3]='b' → False
Option 2 (from s2): s2[1]='b' == s3[3]='b' AND dp[2][1]=True → True

dp[2][2] = True

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   ?   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 7: Fill dp[2][3]
Using s1[0:2]="aa" and s2[0:3]="dbb" → trying to form s3[0:5]="aadbb"

Option 1 (from s1): s1[1]='a' == s3[4]='b' → False
Option 2 (from s2): s2[2]='b' == s3[4]='b' AND dp[2][2]=True → True

dp[2][3] = True

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   T   ?   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 8: Fill dp[2][4]
Using s1[0:2]="aa" and s2[0:4]="dbbc" → trying to form s3[0:6]="aadbbc"

Option 1 (from s1): s1[1]='a' == s3[5]='c' → False
Option 2 (from s2): s2[3]='c' == s3[5]='c' AND dp[2][3]=True → True

dp[2][4] = True

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   T   T   ?
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 9: Fill dp[2][5]
Using s1[0:2]="aa" and s2[0:5]="dbbca" → trying to form s3[0:7]="aadbbcb"

Option 1 (from s1): s1[1]='a' == s3[6]='b' → False
Option 2 (from s2): s2[4]='a' == s3[6]='b' → False

dp[2][5] = False

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   T   T   F
b     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 10: Fill dp[3][1]
Using s1[0:3]="aab" and s2[0:1]="d" → trying to form s3[0:4]="aadb"

Option 1 (from s1): s1[2]='b' == s3[3]='b' AND dp[2][1]=True → True
Option 2 (from s2): s2[0]='d' == s3[3]='b' → False

dp[3][1] = True

      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   T   T   F
b     | F   T   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
c     | F   ?   ?   ?   ?   ?
Step 11: Fill Remaining Cells (Continuing Pattern)
Following the same logic:

dp[3][2]: s1[2]='b'==s3[4]='b' AND dp[2][2]=True → True
dp[3][3]: s1[2]='b'==s3[5]='c' → False; s2[2]='b'==s3[5]='c' → False → False
dp[3][4]: False
dp[3][5]: False

dp[4][1]: s1[3]='c'==s3[4]='b' → False; s2[0]='d'==s3[4]='b' → False → False
dp[4][2]: s1[3]='c'==s3[5]='c' AND dp[3][2]=True → True
dp[4][3]: s1[3]='c'==s3[6]='b' → False; s2[2]='b'==s3[6]='b' AND dp[4][2]=True → True
dp[4][4]: s1[3]='c'==s3[7]='c' AND dp[3][4]=False → False; s2[3]='c'==s3[7]='c' AND dp[4][3]=True → True
dp[4][5]: s1[3]='c'==s3[8]='a' → False; s2[4]='a'==s3[8]='a' AND dp[4][4]=True → True

dp[5][1]: False
dp[5][2]: s1[4]='c'==s3[6]='b' → False; s2[1]='b'==s3[6]='b' AND dp[5][1]=False → False
dp[5][3]: s1[4]='c'==s3[7]='c' AND dp[4][3]=True → True
dp[5][4]: s1[4]='c'==s3[8]='a' → False; s2[3]='c'==s3[8]='a' → False → False
dp[5][5]: s1[4]='c'==s3[9]='c' AND dp[4][5]=True → True
Final DP Table
      | ""  d   b   b   c   a
------|------------------------
""    | T   F   F   F   F   F
a     | T   F   F   F   F   F
a     | T   T   T   T   T   F
b     | F   T   T   F   F   F
c     | F   F   T   T   T   T
c     | F   F   F   T   F   T  ← Answer!
Result: dp[5][5] = True ✅

Key Observations
Each cell depends on: cell above (from s1) OR cell left (from s2)
Indexing: s1[i-1], s2[j-1], s3[i+j-1] (because strings are 0-indexed)
Chain effect: If a cell is False, all cells depending on it will likely be False
Final answer: Bottom-right corner tells us if the entire interleaving is possible
Save this walkthrough! It shows exactly how each decision is made and why the DP approach works. 📝

What is 0-Indexed?
In Python, array/string indices start at 0, not 1.

Example:
s = "hello"

Index:  0    1    2    3    4
        ↓    ↓    ↓    ↓    ↓
Char:   h    e    l    l    o
Apply Code
s[0] = 'h' (first character)
s[1] = 'e' (second character)
s[4] = 'o' (fifth character)
Why This Matters in Our DP Solution
The Confusion:
DP state dp[i][j] talks about "first i characters" → this is counting (1st, 2nd, 3rd...)
String indexing s1[i-1] uses positions (index 0, 1, 2...)
Example with s1 = "aabcc":
i (count)	First i chars	Last char index 	Character
i=1	            "a"	            0	            s1[0]='a'
i=2	            "aa"	        1	            s1[1]='a'
i=3	            "aab"	        2	            s1[2]='b'
i=4	            "aabc"	        3	            s1[3]='c'
i=5	            "aabcc"	        4	            s1[4]='c'
Pattern: If we're using first i characters, the last character is at index i-1.

Why s3[i+j-1]?
When we use:

First i chars from s1
First j chars from s2
Total length = i + j

Total length	Last index in s3	Character
i+j=1	                0	        s3[0]
i+j=2	                1	        s3[1]
i+j=3	                2	        s3[2]
i+j=10	                9	        s3[9]
Pattern: For a string of length L, the last character is at index L-1.

Visual Example: dp[3][1]
s1 = "aabcc"  # indices: 0,1,2,3,4
s2 = "dbbca"  # indices: 0,1,2,3,4
s3 = "aadbbcbcac"  # indices: 0,1,2,3,4,5,6,7,8,9

dp[3][1] → using first 3 chars of s1 + first 1 char of s2
          → "aab" + "d" → trying to form "aadb" (length=4)

Which characters do we compare?
- From s1: s1[2] = 'b'  (3rd char, index=2)
- From s2: s2[0] = 'd'  (1st char, index=0)
- In s3:  s3[3] = 'b'  (4th char, index=3 = 3+1-1)
Apply Code
Contrast: 1-Indexed vs 0-Indexed
Position	1-Indexed	0-Indexed (Python)
1st char	index 1     	index 0
2nd char	index 2     	index 1
3rd char	index 3     	index 2
nth char	index n	        index n-1

Why Do Programming Languages Use 0-Indexing?
Memory addressing: Arrays are stored as offsets from a base address
Mathematical simplicity: Range [0, n) has exactly n elements
Historical reasons: C language influenced most modern languages
Common Mistake to Avoid
# WRONG: Off-by-one error
dp[i][j] = (dp[i-1][j] and s1[i] == s3[i+j])  # ❌

# CORRECT:
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1])  # ✅
Apply Code
Remember: When DP talks about "first i characters" → use index i-1 to access the actual character in the string! 🎯

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Validate if combined lengths match s3 length
        # If not, return False immediately

        # Initialize DP table with dimensions (len(s1)+1) x (len(s2)+1)
        # Set dp[0][0] to True (empty strings can form empty string)

        # Fill base cases for first row (using only s2)
        # For each position j in s2, check if prefix matches s3 prefix

        # Fill base cases for first column (using only s1)
        # For each position i in s1, check if prefix matches s3 prefix

        # Fill DP table using transitions
        # For each cell (i, j) where i > 0 and j > 0:
        #   Option 1: Check if character from s1 matches and dp[i-1][j] is True
        #   Option 2: Check if character from s2 matches and dp[i][j-1] is True
        #   Set dp[i][j] to True if either option is valid

        # Return the value at dp[len(s1)][len(s2)]


         1D array logic
Update Logic Comparison

2D DP:
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
Uses values from previous row (dp[i-1][j]) and left cell (dp[i][j-1])
Both are preserved in the table

1D DP:
dp[j] = (dp[j] and s2[j-1] == s3[i+j-1]) or \
        (dp[j-1] and s1[i-1] == s3[i+j-1])
dp[j] (before update) = dp[i-1][j] from 2D (previous row)
dp[j-1] (already updated) = dp[i][j-1] from 2D (current row, left cell)
Overwrites dp[j] in place

Why It Works
The 1D approach works because:

We only need the previous row (dp[i-1][j]) and current row left cell (dp[i][j-1])
dp[j] before update = value from previous row
dp[j-1] after update = value from current row (already computed)
We iterate j left to right to ensure dp[j-1] is already updated
"""


def isInterleavePossible2D(s1, s2, s3):
        #  base condition
        n = len(s1)
        m = len(s2)
        q = len(s3)

        if q != n + m:
            return False

        dp = [[False] *( len(s2)+ 1 ) for _ in range(len(s1)+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (
                            dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    ) or (
                            dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    )
        return dp[n][m]


def isInterleavePossible1D(s1, s2, s3):
    #  base condition
    n = len(s1)
    m = len(s2)
    q = len(s3)

    if q != n + m:
        return False

    dp = [False] * (len(s2) + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
            elif j==0:
                dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
            else:
                dp[j] = ((dp[j] and s1[i-1] == s3[i+j-1]) or
                         (dp[j-1] and s2[j-1] == s3[i+j-1]))

    return dp[len(s2)]




def main():
    test_cases = [
        ["aabcc", "dbbca", "aadbbcbcac"],
        ["aabcc", "dbbca", "aadbbbaccc"],
        ["", "", ""],
        ["abc", "def", "adbcef"],
        ["abc", "def", "abdecf"]
    ]

    for idx, (s1, s2, s3) in enumerate(test_cases):
        print(f"{idx + 1}.\t Input string: ", s1, s2, s3, sep="\t")
        # result = isInterleavePossible2D(s1, s2, s3)
        result = isInterleavePossible1D(s1, s2, s3)
        print(f"\t isPossible: ", result)
        print("-"*100)



if __name__ == "__main__":
    main()
"""
Here's the complete, corrected trace with all arrays shown at each step:

Input Matrix
Row 0:  1  0  1  0  0
Row 1:  1  0  1  1  1
Row 2:  1  1  1  1  1
Row 3:  1  0  0  1  0
Initialization (Before any row)
height = [0, 0, 0, 0, 0]
left   = [0, 0, 0, 0, 0]
right  = [5, 5, 5, 5, 5]  ← n = 5
max_area = 0
Processing Row 0: 1 0 1 0 0
Step 1: Update height
height = [1, 0, 1, 0, 0]
left   = [0, 0, 0, 0, 0]  ← unchanged yet
right  = [5, 5, 5, 5, 5]  ← unchanged yet
Step 2: Update left (scan left→right, cur_left = 0)
j=0: '1' → left[0] = max(0, 0) = 0
j=1: '0' → cur_left = 2
j=2: '1' → left[2] = max(0, 2) = 2
j=3: '0' → cur_left = 4
j=4: '0' → cur_left = 5

height = [1, 0, 1, 0, 0]
left   = [0, 0, 2, 0, 0]  ← updated
right  = [5, 5, 5, 5, 5]  ← unchanged yet
Step 3: Update right (scan right→left, cur_right = 5)
j=4: '0' → cur_right = 4
j=3: '0' → cur_right = 3
j=2: '1' → right[2] = min(5, 3) = 3
j=1: '0' → cur_right = 1
j=0: '1' → right[0] = min(5, 1) = 1

height = [1, 0, 1, 0, 0]
left   = [0, 0, 2, 0, 0]
right  = [1, 5, 3, 5, 5]  ← updated
Step 4: Calculate areas
j=0: 1 × (1 - 0) = 1
j=1: 0 × (5 - 0) = 0
j=2: 1 × (3 - 2) = 1
j=3: 0 × (5 - 0) = 0
j=4: 0 × (5 - 0) = 0

max_area = max(0, 1, 0, 1, 0, 0) = 1
Processing Row 1: 1 0 1 1 1
Step 1: Update height
height = [2, 0, 2, 1, 1]
left   = [0, 0, 2, 0, 0]  ← from previous row
right  = [1, 5, 3, 5, 5]  ← from previous row
Step 2: Update left (scan left→right, cur_left = 0)
j=0: '1' → left[0] = max(0, 0) = 0
j=1: '0' → cur_left = 2
j=2: '1' → left[2] = max(2, 2) = 2
j=3: '1' → left[3] = max(0, 2) = 2
j=4: '1' → left[4] = max(0, 2) = 2

height = [2, 0, 2, 1, 1]
left   = [0, 0, 2, 2, 2]  ← updated
right  = [1, 5, 3, 5, 5]  ← unchanged yet
Step 3: Update right (scan right→left, cur_right = 5)
j=4: '1' → right[4] = min(5, 5) = 5
j=3: '1' → right[3] = min(5, 5) = 5
j=2: '1' → right[2] = min(3, 5) = 3  ← constraint from Row 0 persists!
j=1: '0' → cur_right = 1
j=0: '1' → right[0] = min(1, 1) = 1

height = [2, 0, 2, 1, 1]
left   = [0, 0, 2, 2, 2]
right  = [1, 5, 3, 5, 5]  ← updated
Step 4: Calculate areas
j=0: 2 × (1 - 0) = 2
j=1: 0 × (5 - 0) = 0
j=2: 2 × (3 - 2) = 2
j=3: 1 × (5 - 2) = 3
j=4: 1 × (5 - 2) = 3

max_area = max(1, 2, 0, 2, 3, 3) = 3
Processing Row 2: 1 1 1 1 1
Step 1: Update height
height = [3, 1, 3, 2, 2]
left   = [0, 0, 2, 2, 2]  ← from previous row
right  = [1, 5, 3, 5, 5]  ← from previous row
Step 2: Update left (scan left→right, cur_left = 0)
j=0: '1' → left[0] = max(0, 0) = 0
j=1: '1' → left[1] = max(0, 0) = 0
j=2: '1' → left[2] = max(2, 0) = 2  ← constraint from Row 1 persists!
j=3: '1' → left[3] = max(2, 0) = 2
j=4: '1' → left[4] = max(2, 0) = 2

height = [3, 1, 3, 2, 2]
left   = [0, 0, 2, 2, 2]  ← updated
right  = [1, 5, 3, 5, 5]  ← unchanged yet
Step 3: Update right (scan right→left, cur_right = 5)
j=4: '1' → right[4] = min(5, 5) = 5
j=3: '1' → right[3] = min(5, 5) = 5
j=2: '1' → right[2] = min(3, 5) = 3  ← constraint from Row 0 still persists!
j=1: '1' → right[1] = min(5, 5) = 5
j=0: '1' → right[0] = min(1, 5) = 1  ← constraint from Row 0 persists!

height = [3, 1, 3, 2, 2]
left   = [0, 0, 2, 2, 2]
right  = [1, 5, 3, 5, 5]  ← updated
Step 4: Calculate areas
j=0: 3 × (1 - 0) = 3
j=1: 1 × (5 - 0) = 5
j=2: 3 × (3 - 2) = 3
j=3: 2 × (5 - 2) = 6  ← MAX FOUND!
j=4: 2 × (5 - 2) = 6  ← MAX FOUND!

max_area = max(3, 3, 5, 3, 6, 6) = 6 ✓
Processing Row 3: 1 0 0 1 0
Step 1: Update height

height = [4, 0, 0, 3, 0]
left   = [0, 0, 2, 2, 2]  ← from previous row
right  = [1, 5, 3, 5, 5]  ← from previous row
Step 2: Update left (scan left→right, cur_left = 0)
j=0: '1' → left[0] = max(0, 0) = 0
j=1: '0' → cur_left = 2
j=2: '0' → cur_left = 3
j=3: '1' → left[3] = max(2, 3) = 3
j=4: '0' → cur_left = 5

height = [4, 0, 0, 3, 0]
left   = [0, 0, 0, 3, 0]  ← updated
right  = [1, 5, 3, 5, 5]  ← unchanged yet
Step 3: Update right (scan right→left, cur_right = 5)
j=4: '0' → cur_right = 4
j=3: '1' → right[3] = min(5, 4) = 4
j=2: '0' → cur_right = 2
j=1: '0' → cur_right = 1
j=0: '1' → right[0] = min(1, 1) = 1

height = [4, 0, 0, 3, 0]
left   = [0, 0, 0, 3, 0]
right  = [1, 5, 5, 4, 5]  ← updated
Step 4: Calculate areas
j=0: 4 × (1 - 0) = 4
j=1: 0 × (5 - 0) = 0
j=2: 0 × (5 - 0) = 0
j=3: 3 × (4 - 3) = 3
j=4: 0 × (5 - 0) = 0

max_area = max(6, 4, 0, 0, 3, 0) = 6 (unchanged)
Final Result
max_area = 6 ✓
Key observation: The constraints in left and right arrays persist across rows until overridden by new zeros in the current row. This is why right[2] stays at 3 throughout - the zero at Row 0, column 3 blocks column 2 from expanding rightward in all subsequent rows!
Excellent question! This is the heart of the algorithm. Let me explain with a concrete scenario:

The Constraint Logic
Think of left[j] and right[j] as boundaries that the rectangle cannot cross:

left[j] = "You cannot extend left of this column"
right[j] = "You cannot extend right of this column"
When we have two constraints (from previous rows AND current row), the rectangle must satisfy BOTH. So we take the more restrictive boundary.

Why max for Left?
Scenario:

Previous rows constraint: "Can't go left of column 2" (because there was a zero at column 1 above)
Current row constraint: "Can't go left of column 0" (no zero blocking in current row)
Question: Where can the rectangle actually start?

If we start at column 0: ❌ Violates the previous row's constraint (would include the zero above)
If we start at column 2: ✅ Satisfies both constraints
Answer: We must take max(2, 0) = 2 ← the stricter constraint

Why min for Right?
Scenario:

Previous rows constraint: "Can't go right of column 5" (no blocking above)
Current row constraint: "Can't go right of column 3" (there's a zero at column 3 in current row)
Question: Where can the rectangle actually end?

If we end at column 5: ❌ Violates the current row's constraint (would include the zero in this row)
If we end at column 3: ✅ Satisfies both constraints
Answer: We must take min(5, 3) = 3 ← the stricter constraint

Visual Example
Row 0:  1  0  1  1  1
Row 1:  1  1  1  1  1
        ↓  ↓  ↓  ↓  ↓
At column 2, Row 1:

Previous row left[2] = 2 (blocked by zero at column 1 in Row 0)
Current row cur_left = 0 (no zero blocking in Row 1)
Result: left[2] = max(2, 0) = 2 ← still blocked by the zero above!
At column 0, Row 1:

Previous row right[0] = 1 (blocked by zero at column 1 in Row 0)
Current row cur_right = 5 (no zero blocking in Row 1)
Result: right[0] = min(1, 5) = 1 ← still blocked by the zero above!
The Rule
Boundary	Operation	Why
left[j]	max(prev_left, cur_left)	Take the rightmost start position (more restrictive)
right[j]	min(prev_right, cur_right)	Take the leftmost end position (more restrictive)
Think of it this way: The rectangle is being "squeezed" by constraints from all directions. We take whichever constraint is tighter at each boundary.

Does this make sense now?

so if that is the case area should be added tp previous row area right ? why we do max


Leet
Thought for 9s

Great question! This reveals a key conceptual point about what we're actually computing.

We're Finding the Maximum Single Rectangle, Not a Sum
Think about what the problem asks: "Find the largest rectangle containing only 1's"

Each position (i,j) represents the bottom edge of a potential rectangle. When we compute area = height[j] * (right[j] - left[j]), we're calculating the area of one specific rectangle that ends at the current row.

Why Max, Not Sum?
Example from Row 1:

Row 0 area: [1, 0, 1, 0, 0] → max = 1
Row 1 area: [2, 0, 6, 3, 3] → max = 6
If we summed these: 1 + 6 = 7 ❌
But the actual answer is 6 ✅

Why? Because:

The area 1 from Row 0 was a 1×1 rectangle at column 0
The area 6 from Row 1 is a 2×3 rectangle spanning columns 2-4
These are different rectangles - we want the largest one, not their combined area
The DP State vs. The Result
Component	Accumulates?	Why
height[j]	✅ Yes	Counts consecutive 1's vertically
left[j]	✅ Yes	Remembers leftmost boundary from all rows above
right[j]	✅ Yes	Remembers rightmost boundary from all rows above
area	❌ No	Represents one rectangle at current position
max_area	✅ Yes (via max)	Tracks the best rectangle found so far

if i assume correctly then very row is a histogram base. I would like to know how one row's left and right contribute to the next row


Leet
Thought for 7s

Excellent observation! Yes, each row acts as a histogram base. Let me show you exactly how the previous row's left and right constrain the current row:

The Propagation Rule
left[j]  = max(previous_row_left[j],  current_row_cur_left)
right[j] = min(previous_row_right[j], current_row_cur_right)
Why max for left, min for right?

The rectangle must satisfy both the vertical constraint (from above rows) and the horizontal constraint (current row)
For left boundary: we can't go left of either constraint → take the rightmost (max) of the two
For right boundary: we can't go right of either constraint → take the leftmost (min) of the two
Concrete Example: Row 1 → Row 2
After Row 1: 1 0 1 1 1

height: [2, 0, 2, 1, 1]
left:   [0, 0, 2, 2, 2]   ← from previous row
right:  [1, 5, 5, 5, 5]   ← from previous row
Processing Row 2: 1 1 1 1 1

Left pass (current row has no zeros, so cur_left stays 0):

j=0: left[0] = max(0, 0) = 0  ← kept previous row's 0
j=1: left[1] = max(0, 0) = 0  ← previous row had 0, now can extend to 0
j=2: left[2] = max(2, 0) = 2  ← previous row's constraint (column 1 was zero) still applies!
j=3: left[3] = max(2, 0) = 2  ← same constraint
j=4: left[4] = max(2, 0) = 2  ← same constraint
Key insight: Even though Row 2 has all 1's, the zero at column 1 in Row 1 still blocks columns 2-4 from extending left past column 2. The constraint propagates downward!

Right pass (current row has no zeros, so cur_right stays 5):

j=4: right[4] = min(5, 5) = 5
j=3: right[3] = min(5, 5) = 5
j=2: right[2] = min(5, 5) = 5
j=1: right[1] = min(5, 5) = 5
j=0: right[0] = min(1, 5) = 1  ← previous row's constraint (column 0 was blocked by column 1's zero)
Final after Row 2:

height: [3, 1, 3, 2, 2]
left:   [0, 0, 2, 2, 2]  ← notice columns 2-4 still can't go left past 2!
right:  [1, 5, 5, 5, 5]
Why This Matters
The rectangle at column 2 in Row 2 has:

height = 3 (three consecutive 1's above)
left = 2 (blocked by the zero at column 1 in Row 1)
right = 5 (no blockage to the right)
area = 3 × (5 - 2) = 9
Think of it this way: The left and right arrays represent "memory" of where zeros have appeared in the entire column stack above the current row. They persist until a new zero in the current row overrides them.

Does this clarify how the constraints propagate vertically through the DP state?


When matrix[i][j] == '0':
For the current cell j itself:

height[j] = 0 (resets completely)
left[j] and right[j] are still computed, but don't matter since height is 0 (area = 0)
For OTHER cells (the important part):

Left boundary propagation:
When we scan left→right and hit a zero at column j:

if matrix[i][j] == '0':
    cur_left = j + 1  # ← This affects FUTURE columns to the RIGHT
    height[j] = 0
else:
    left[j] = max(left[j], cur_left)  # Uses the most recent zero's position
Apply Code
Example from Row 1:

Row:    1  0  1  1  1
        ↓  ↓  ↓  ↓  ↓
cur_left: 0→1→2→2→2  # After hitting zero at j=1, cur_left=2
left[j]: [0, ?, 2, 2, 2]  # Columns 2,3,4 can't extend left past j=1
Right boundary propagation:
When we scan right→left and hit a zero at column j:

if matrix[i][j] == '0':
    cur_right = j  # ← This affects FUTURE columns to the LEFT
    height[j] = 0
else:
    right[j] = min(right[j], cur_right)  # Uses the most recent zero's position
Apply Code
Example from Row 1 (scanning right→left):

Row:      1  1  1  0  1
          ←  ←  ←  ←  ←
cur_right:5→5→5→3→3  # After hitting zero at j=3, cur_right=3
right[j]: [3, 3, 3, ?, 5]  # Columns 0,1,2 can't extend right past j=3
Key Insight
The zero at position j doesn't "reset" left[j] and right[j] for itself—it blocks other columns from extending their rectangles across this zero.
"""


def maximalRectangle(matrix):
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    left = [0] * n
    right = [n] * n
    height = [0] * n

    maxArea = 0

    for i in range(m):
        curleft = 0
        curRight = n

        for j in range(n):
            if matrix[i][j] == '1':
                height[j] += 1
                left[j] = max(left[j], curleft)
            else:
                height[j] = 0
                left[j] = 0
                curleft = j+1

        for j in range(n-1, -1,-1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], curRight)
            else:
                right[j] = n
                curRight = j

            maxArea = max(maxArea, (right[j] - left[j]) * height[j])

    return maxArea

def main():
    matrices = [
        [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']
        ],
        [
            ['0', '1'],
            ['1', '1']
        ],
        [
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1']
        ],
        [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ],
        [
            ['1']
        ]
    ]

    for i, matrix in  enumerate(matrices):
        result = maximalRectangle(matrix)
        print("\t i+1. Given matrix ", matrix)
        print("\t area: ",result)
        print("-"*100)


if __name__ == "__main__":
    main()
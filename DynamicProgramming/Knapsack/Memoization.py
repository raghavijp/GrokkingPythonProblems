def find_kanpsack_profit_memoization_helper(weights, values, capacity, dp, n):
    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n-1] <= capacity:
        dp[n][capacity] = max( values[n-1] + find_kanpsack_profit_memoization_helper(weights, values, capacity - weights[n-1], dp, n-1),
                               find_kanpsack_profit_memoization_helper(weights, values, capacity , dp, n-1))
        return dp[n][capacity]

    dp[n][capacity] = find_kanpsack_profit_memoization_helper(weights, values, capacity , dp, n-1)
    return dp[n][capacity]


def find_kanpsack_profit_memoization(weights, values, capacity):
    n = len(weights)
    dp = [[-1 for i in range (capacity + 1)] for j in range(n+1) ]
    
    return find_kanpsack_profit_memoization_helper(weights, values, capacity, dp, n)


def main():
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]

    for i in range(len(weights)):
        print(f"\t weights:", weights[i])
        print(f"\t values:", values[i])
        print(f"\t capacity:", capacity[i])
        print(f"\t Maximum Items:", find_kanpsack_profit_memoization(weights[i], values[i], capacity[i]))
        print("*" * 100)


if __name__ == "__main__":
    main()

"""
Step-by-step walkthrough of the memoization code with the example:
Given:

values = [3, 5, 2, 7]
weights = [3, 1, 2, 4]
capacity = 5
n = 4 (number of items)
Initial call: knapsack_memo(5, weights, values, 4, memo)

Checks if item 4 (weight 4) can fit in capacity 5 → yes
Two choices:
Include item 4: value = 7 + knapsack_memo(5 - 4 = 1, weights, values, 3, memo)
Exclude item 4: knapsack_memo(5, weights, values, 3, memo)
Include item 4: knapsack_memo(1, weights, values, 3, memo)

Item 3 weight = 2, which is > capacity 1, so cannot include
Move to next item: knapsack_memo(1, weights, values, 2, memo)
At item 2 with capacity 1: knapsack_memo(1, weights, values, 2, memo)

Item 2 weight = 1, fits in capacity 1
Choices:
Include: value = 5 + knapsack_memo(1 - 1 = 0, weights, values, 1, memo)` → capacity 0 means return 0
Exclude: knapsack_memo(1, weights, values, 1, memo)
Include item 2: returns 5 + 0 = 5

Exclude item 2: knapsack_memo(1, weights, values, 1, memo)

Item 1 weight = 3, which is > capacity 1, cannot include
Move to next item: knapsack_memo(1, weights, values, 0, memo) → 0 items means return 0
So, max for item 2 with capacity 1 is max(5, 0) = 5

Back to step 2: max value including item 4 = 7 + 5 = 12

Exclude item 4: knapsack_memo(5, weights, values, 3, memo)

Item 3 weight = 2, fits in capacity 5
Choices:
Include: 2 + knapsack_memo(5 - 2 = 3, weights, values, 2, memo)
Exclude: knapsack_memo(5, weights, values, 2, memo)
This process continues recursively, storing results in memo.

Memoization effect:

Once knapsack_memo(3, weights, values, 2, memo) is computed, it is saved.
If the same subproblem is needed again, the stored value is returned immediately, avoiding repeated work.
This example shows how the recursion tree is pruned by memoization, improving efficiency drastically.

If you want, I can provide a detailed recursion tree or explain any specific part further!

Recursion Tree for Memoization in 0/1 Knapsack
Using the example:

values = [3, 5, 2, 7]
weights = [3, 1, 2, 4]
capacity = 5
n = 4 (items)
knapsack_memo(5, 4)
|
|-- Include item 4 (weight 4): 7 + knapsack_memo(1, 3)
|   |
|   |-- Item 3 (weight 2) > capacity 1, cannot include
|   |   |
|   |   |-- knapsack_memo(1, 2)
|   |       |
|   |       |-- Include item 2 (weight 1): 5 + knapsack_memo(0, 1) = 5 + 0 = 5
|   |       |
|   |       |-- Exclude item 2: knapsack_memo(1, 1)
|   |           |
|   |           |-- Item 1 (weight 3) > capacity 1, cannot include
|   |           |   |
|   |           |   |-- knapsack_memo(1, 0) = 0
|   |           |
|   |           `-- Returns 0
|   |       |
|   |       `-- Max(5, 0) = 5
|   |
|   `-- Returns 5
|
|-- Exclude item 4: knapsack_memo(5, 3)
    |
    |-- Include item 3 (weight 2): 2 + knapsack_memo(3, 2)
    |   |
    |   |-- Include item 2 (weight 1): 5 + knapsack_memo(2, 1)
    |   |   |
    |   |   |-- Item 1 (weight 3) > capacity 1, cannot include
    |   |   |   |
    |   |   |   `-- knapsack_memo(1, 0) = 0
    |   |   |
    |   |   `-- Returns 0
    |   |   |
    |   |   `-- Max(5 + 0, knapsack_memo(2, 1))
    |   |
    |   `-- Exclude item 2: knapsack_memo(3, 1)
    |       ... (similar to above)
    |
    |-- Exclude item 3: knapsack_memo(5, 2)
        ... (similar recursive calls)

Key points:
Each node represents a call with parameters (capacity, n).
Branches represent the choice to include or exclude the current item.
Memoization stores results at each (capacity, n) to avoid recomputation.

Visual Diagram of the Memoization Recursion Tree
Here’s a simple textual visualization of the recursion tree with memoization for the 0/1 Knapsack example:

knapsack_memo(cap=5, n=4)
├── Include item 4 (weight=4, value=7): 7 + knapsack_memo(cap=1, n=3)
│   ├── Item 3 (weight=2) > cap=1 → skip
│   └── knapsack_memo(cap=1, n=2)
│       ├── Include item 2 (weight=1, value=5): 5 + knapsack_memo(cap=0, n=1) = 5 + 0 = 5
│       └── Exclude item 2: knapsack_memo(cap=1, n=1)
│           ├── Item 1 (weight=3) > cap=1 → skip
│           └── knapsack_memo(cap=1, n=0) = 0
│       └── Max(5, 0) = 5
│   └── Returns 5
├── Exclude item 4: knapsack_memo(cap=5, n=3)
│   ├── Include item 3 (weight=2, value=2): 2 + knapsack_memo(cap=3, n=2)
│   │   ├── Include item 2 (weight=1, value=5): 5 + knapsack_memo(cap=2, n=1)
│   │   │   ├── Item 1 (weight=3) > cap=2 → skip
│   │   │   └── knapsack_memo(cap=2, n=0) = 0
│   │   │   └── Returns 0
│   │   │   └── Max(5 + 0, knapsack_memo(cap=2, n=1))
│   │   └── Exclude item 2: knapsack_memo(cap=3, n=1)
│   │       └── ... (similar calls)
│   └── Exclude item 3: knapsack_memo(cap=5, n=2)
│       └── ... (similar calls)
└── Returns max of include/exclude
How memoization improves efficiency:
Each unique subproblem (capacity, n) is computed once and stored.
Repeated calls with the same parameters fetch the stored result instantly.
This avoids exponential recomputation, reducing time complexity significantly.
If you want, I can help you create a more graphical representation or explain any specific branch in detail.

Would you like me to proceed with that?

yes
Graphical Representation of Memoization Recursion Tree
Here is a more structured graphical view of the recursion tree for the 0/1 Knapsack example:

knapsack_memo(cap=5, n=4)
├── Include item 4 (weight=4, value=7)
│   └── knapsack_memo(cap=1, n=3)
│       ├── Skip item 3 (weight=2 > cap=1)
│       └── knapsack_memo(cap=1, n=2)
│           ├── Include item 2 (weight=1, value=5)
│           │   └── knapsack_memo(cap=0, n=1) = 0
│           └── Exclude item 2
│               └── knapsack_memo(cap=1, n=1)
│                   ├── Skip item 1 (weight=3 > cap=1)
│                   └── knapsack_memo(cap=1, n=0) = 0
├── Exclude item 4
│   └── knapsack_memo(cap=5, n=3)
│       ├── Include item 3 (weight=2, value=2)
│       │   └── knapsack_memo(cap=3, n=2)
│       │       ├── Include item 2 (weight=1, value=5)
│       │       │   └── knapsack_memo(cap=2, n=1)
│       │       │       ├── Skip item 1 (weight=3 > cap=2)
│       │       │       └── knapsack_memo(cap=2, n=0) = 0
│       │       └── Exclude item 2
│       │           └── knapsack_memo(cap=3, n=1)
│       └── Exclude item 3
│           └── knapsack_memo(cap=5, n=2)
Explanation:
Each node shows the function call with current capacity and number of items considered.
Branches show the choice to include or exclude the current item.
When an item’s weight exceeds the current capacity, that branch is skipped.
Memoization stores results at each node, so repeated calls with the same parameters return instantly.
This structure helps visualize how the problem breaks down into smaller subproblems and how memoization prevents redundant calculations.


"""
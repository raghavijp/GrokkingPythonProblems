def find_partition_array(arr):

    array_sum = sum(arr)

    if array_sum % 2 != 0:
        return False

    subset_sum = array_sum // 2

    #Initialize False for all cols . First column except [0][0] is False as empty subsets cannot have sum more than 0
    dp = [[False for i in range(len(arr) + 1)] for j in range(subset_sum + 1)]

    for col in range(len(arr) + 1):
        dp[0][col] = True # all subsets can have 0 as their sum

    for i in range(1, subset_sum + 1):
        for j in range(1, len(arr) + 1):

            if (arr[j-1] > i):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-arr[j-1]][j-1] or dp[i][j-1]

    return dp[-1][-1]


def main():
    arr = [[3, 1, 1, 2, 2, 1], [1, 3, 7, 3], [1, 2, 3], [1, 2, 5],
           [1, 3, 4, 8], [1, 2, 3, 2, 3, 5], [1, 5, 3, 2, 3, 19, 3],
           [1, 2, 3, 5, 3, 2, 1]]

    for i in range(len(arr)):
        print(f"\t Given Array: ", arr[i])
        print(f"\t The above array can be partitioned :", find_partition_array(arr[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
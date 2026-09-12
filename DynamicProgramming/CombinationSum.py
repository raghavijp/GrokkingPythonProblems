def find_combinations_target(nums, target):
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])

    for i in range(1, target+1):
        for j in range(len(nums)):

            if nums[j] <= i:

                for prev in dp[i-nums[j]]:
                    temp = prev + [nums[j]]
                    temp.sort()

                    if temp not in dp[i]:
                        dp[i].append(temp)

    return dp[target]


def main():
    nums = [
        [2, 3, 5],
        [3, 6, 7, 8],
        [4, 5, 6, 9],
        [20, 25, 30, 35, 40],
        [3, 5, 7]
    ]

    targets = [5, 15, 11, 40, 15]
    for i in range(len(nums)):
        print(f"\t Given Array :", nums[i], end="")
        print(f"\t Target: ", targets[i])
        combinations = find_combinations_target(nums[i], targets[i])
        print(f"\t Combinations: ", combinations)
        print("-"*100)

if __name__ == "__main__":
    main()
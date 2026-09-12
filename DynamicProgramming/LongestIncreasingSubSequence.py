def calculateLength(nums):
    n = len(nums)

    length = [1] * n
    count = [1] * n

    maxLen = 1

    for i in range(n):
        for j in range(i):

            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1;
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] = count[i] + count[j]

        maxLen = max(maxLen, length[i])

    result = 0
    for i in range(n):
        if length[i] == maxLen:
            result = result + count[i]

    return result

def main():
    arrs = [
        [1, 2, 3, 4, 5],
        [8, 8, 8, 8, 8, 8],
        [50, 60, 40, 80, 70],
        [2, 1, 3, 2, 4],
        [1, 2, 4, 3, 5, 4, 6]
    ]

    for i, nums in enumerate(arrs):
        print(f"\t {i+1}. Given Array: ", nums)
        print(f"\t longestSequence length: ", calculateLength(nums))
        print("-"*100)


if __name__ == "__main__":
    main()
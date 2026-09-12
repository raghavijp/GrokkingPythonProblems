def find_max_product_arr(nums):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]

        prev_max_so_far = max_so_far
        max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, prev_max_so_far * curr, min_so_far * curr)
        result = max (max_so_far, result)

    return result


def main():
    input = [
        [-2, 0, -1],
        [2, 3, -2, 4],
        [2, -5, 3, 1, -4, 0, -10, 2],
        [1, 2, 3, 0, 4],
        [5, 4, 3, 10, 4, 1],
    ]

    for i in range(len(input)):
        print(f"\t Given Array :", input[i])
        print(f"\t Maximum Product :", find_max_product_arr(input[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
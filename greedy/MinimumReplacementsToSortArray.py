def minimumReplacement(nums):
    operations = 0
    n = len(nums)

    for i in range(n-2,-1,-1):
        if nums[i] > nums[i+1]:
            parts = (nums[i] + nums[i+1] -1) // nums[i+1]
            operations += parts - 1
            nums[i] = nums[i] // parts

    return operations

def main():
        test_cases = [
            [3, 9, 3],
            [1, 2, 3, 4, 5],
            [5, 6, 7],
            [10, 5, 1],
            [1000000000, 1]
        ]


        for i, nums in enumerate(test_cases, 1):
            print("\tnums:", nums)
            result = minimumReplacement(nums)
            print("\tMinimum operations:", result)
            print("-" * 100)

if __name__ == "__main__":
    main()


"""
Why Add nums[i + 1] - 1 Before Division?
The goal is to perform ceiling division, which means rounding up the result of division when there’s a remainder.

Normally, integer division truncates (rounds down) the result. For example, 7 / 3 = 2 (not 2.33).
To round up, we add a value just enough to push the division result to the next integer if there is any remainder.
How adding nums[i + 1] - 1 works:

Suppose we want to divide a by b and get the ceiling of a / b.
If a is exactly divisible by b, adding b - 1 won’t push it over to the next integer.
If a is not divisible by b, adding b - 1 increases a enough so that integer division rounds up.
Example:

a = 7, b = 3

Normal division: 7 / 3 = 2 (integer division)

Add b - 1: 7 + 3 - 1 = 9

Now divide: 9 / 3 = 3 (ceiling division)

If a was divisible, say 6 / 3:

6 + 3 - 1 = 8
8 / 3 = 2 (still correct, no rounding up)
This trick ensures the division result is always rounded up without using floating-point operations.

"""
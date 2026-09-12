class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x


def largestNumber(nums):
    nums_string = [str(num) for num in nums]
    nums_string.sort(key=LargerNumKey);

    if nums_string[0] == "0":
        return 0

    return ''.join(nums_string)


def main():
    tests = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [0, 0, 0],
        [12, 121],
        [34, 5, 92, 7]
    ]

    for i , test in enumerate(tests):
        print(f"{i} \t . Input {test}")
        print(f'\n\t Largest Number: "{largestNumber(test)}"')
        print("*" * 100)

main()
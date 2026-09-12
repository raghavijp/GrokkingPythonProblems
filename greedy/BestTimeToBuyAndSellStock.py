def profit(test):
    profit = 0
    for i in range(1, len(test)):
        if test[i] - test[i-1] > 0:
            profit += test[i] - test[i-1]

    return profit


def main():
    testCases=[
        [4, 1, 5, 2, 9, 3, 7],
        [8, 2, 6, 4, 7, 5],
        [7, 6, 4, 3, 1],
        [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8],
        [1, 2]
    ]

    for i , test in enumerate(testCases):
        print(f'Given array: {test}')
        print(f'profit: "{profit(test)}"')



main()
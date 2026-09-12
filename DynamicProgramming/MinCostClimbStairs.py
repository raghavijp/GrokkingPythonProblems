def calculateCost(arr):

    down1 = 0
    down2 = 0

    for i in range(2, len(arr) + 1 ):

        down1 , down2 =( min(down1 + arr[i-1], down2 + arr[i-2]) , down1 )


    return down1

def main():
    testCases = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1],
        [0, 1, 0, 1, 0, 1]
    ]

    for i, arr in enumerate(testCases):
        print(f"\t {i+1}. Given array: ",arr)
        print(f"\t Min Cost: ",calculateCost(arr))
        print("-"*100)


if __name__ == "__main__":
    main()
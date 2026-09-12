def distributeCandy(ratings):
    n = len(ratings)
    candies=[1] * n

    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i],candies[i+1] + 1)


    return sum(candies)

def main():
    test_cases = [
        [1, 0, 2],
        [1, 2, 2],
        [1, 3, 4, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]

    for i, ratings in enumerate(test_cases, 1):
        print(i, "\tratings =", ratings)
        result = distributeCandy(ratings)
        print("\tMinimum candies =", result)
        print("-"*100)
if __name__ == "__main__":
    main()

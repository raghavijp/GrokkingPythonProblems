from collections import Counter

def min_cost_to_Arrange_fruits(basket1, basket2):
    combined = basket1 + basket2
    combined_counter = Counter(combined)

    for count in combined_counter.values():
        if  count % 2 != 0:
            return -1

    counter1 = Counter(basket1)
    counter2 = Counter(basket2)

    excess1 = []
    excess2 = []

    for fruit in combined_counter:
        diff = counter1[fruit] - counter2[fruit]
        if diff > 0:
            excess1.extend([fruit] * (diff // 2))
        elif diff < 0:
            excess2.extend([fruit] * (-diff // 2))

    excess1.sort()
    excess2.sort(reverse=True)

    min_fruit_cost = min(combined_counter.keys())
    print("cost \t", min_fruit_cost)
    print("#" * 10)


    for element in excess1:
        print(element)
    print("*" * 10)
    for value in excess2:
        print(value)



    total_cost = 0
    ###This considers either directly swapping the two fruits or
    # using two operations with the cheapest available fruit as an intermediary, whichever costs less.
    for i in range(len(excess1)):
        total_cost += min(2 * min_fruit_cost, excess1[i],excess2[i])

    return total_cost


def main():
    testCases = [
        [[4, 2, 2, 2], [1, 4, 1, 2]],
        [[2, 3, 4, 1], [3, 2, 5, 1]],
        [[84, 80, 43, 8, 80, 88, 43, 14, 100, 88], [32, 32, 42, 68, 68, 100, 42, 84, 14, 8]],
        [[1, 2, 2, 3, 3, 4], [1, 1, 2, 3, 4, 4]],
        [[4, 4, 4, 4, 3], [5, 5, 5, 5, 3]]
    ]

    for i , test_case in enumerate(testCases):
        print(i+1,". \t Basket 1", testCases[i][0], sep="")
        print("\t Basket 2 = ", testCases[i][1], sep="")
        
        result = min_cost_to_Arrange_fruits(testCases[i][0], testCases[i][1])
        print("\n \t Min Cost to arrange fruits", result, sep="")
        print("-" * 100)


main()

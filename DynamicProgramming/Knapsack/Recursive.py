def find_max_items_helper(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if (weights[n-1] <= capacity):
        return max(values[n-1] + find_max_items_helper(weights, values, capacity - weights[n-1], n-1),
                   find_max_items_helper(weights, values, capacity, n-1))
    else:
        return find_max_items_helper(weights, values, capacity, n - 1)


def find_kanpsack_profit(weights, values, capacity):
    n = len(weights)
    return find_max_items_helper(weights, values, capacity, n)


def main():
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]

    for i in range(len(weights)):
        print(f"\t weights:", weights[i])
        print(f"\t values:", values[i])
        print(f"\t capacity:", capacity[i])
        print(f"\t Maximum Items:", find_kanpsack_profit(weights[i], values[i], capacity[i]))
        print("*" * 100)

if __name__ == "__main__":
    main()
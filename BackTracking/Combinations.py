def combine(n, k):
    ans = []
    def backtrackCombinations(path, start):

        if len(path) == k:
            ans.append(path[:])
            return

        need = k - len(path)

        max_start = n - need + 1

        for num in range(start, max_start + 1):
            path.append(num)
            backtrackCombinations(path, num + 1)
            path.pop()

    backtrackCombinations([], 1)
    return ans


if __name__ =="__main__":
    n_values = [4, 4, 5, 5, 6]
    k_values = [2, 3, 2, 3, 4]

    for i in range(len(n_values)):
        print(i + 1, "\tn:", n_values[i])
        print("\tk:", k_values[i])
        result = combine(n_values[i], k_values[i])
        print("\n\tcombinations:", result)
        print("-" * 100)
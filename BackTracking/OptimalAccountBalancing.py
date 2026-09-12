import collections

def dfs(current, n, balance):
     while current < n and not balance[current]:
         current += 1

     if current == n:
         return 0

     cost = float('inf')

     for next in range(current + 1, n):
         if balance[current] * balance[next] < 0:
             balance[next] += balance[current]
             cost = min(cost, 1 + dfs(current + 1, n, balance))
             balance[next] -= balance[current]

     return cost

def min_transfers(transactions):
    balance_map = collections.defaultdict(int)
    for a, b, amount in transactions:
        balance_map[a] += amount
        balance_map[b] -= amount

    balance = [amount for amount in balance_map.values() if amount]

    n = len(balance)
    return dfs(0, n, balance,)



def main():
    transactions = [[[0, 1, 40], [1, 2, 15], [0, 3, 30], [4, 5, 10], [2, 5, 10]],
                    [[1, 0, 10], [2, 0, 30], [3, 0, 40], [2, 0, 15]],
                    [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60]],
                    [[0, 1, 10], [0, 2, 20], [0, 3, 30], [0, 4, 40], [5, 0, 100]],
                    [[0, 1, 10], [1, 0, 10]]]

    for i in range(len(transactions)):
        print(i + 1, ".\tTransactions:", transactions[i])
        print("\n\tMinimum number of transactions to settle all debts:", min_transfers(transactions[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
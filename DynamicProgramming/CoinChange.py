def calculate_minimum_coins(coins, remaining_amount, counter):
    if remaining_amount < 0:
        return -1
    if remaining_amount == 0:
        return 0
    if counter[remaining_amount - 1] != float('inf'):
        return counter[remaining_amount - 1]
    minimum = float('inf')

    for s in coins:
        result = calculate_minimum_coins(coins, remaining_amount - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    counter[remaining_amount - 1] =  minimum if minimum !=  float('inf') else  -1
    return counter[remaining_amount - 1]

def coin_change(coins, total):
    if total < 1:
        return 0
    return calculate_minimum_coins(coins, total, [float('inf')] * total)


# Driver Code

def main():

    coins = [[1, 3, 4, 5], [1, 4, 6, 9], [6, 7, 8], [1, 2, 3, 4, 5], [14, 15, 18, 20]]
    total = [7, 11, 27, 41, 52]

    for i in range(len(total)):
        print(str(i+1) + ".\tThe minimum number of coins required to find " + str(total[i]) + " from " + str(coins[i]) + " is: " + str(coin_change(coins[i], total[i])))
        print("-" * 100)

if __name__ == '__main__':
    main()

"""
How the memoization table (counter) evolves for coins = [1, 3, 4, 5] and total = 7:
Initially, counter is [-1, -1, -1, -1, -1, -1, -1, -1] (size 8 for amounts 0 to 7).

Base case: counter[0] = 0 implicitly by returning 0 when remaining is 0.

When calculate_minimum_coins(1) is called:

Tries coins:
1: calculate_minimum_coins(0) returns 0 → minimum = 1
3, 4, 5: calls with negative remaining → return -1
So, counter[1] = 1

When calculate_minimum_coins(2):
Coins:
1: calculate_minimum_coins(1) = 1 → minimum = 2
3,4,5: negative remaining → -1
counter[2] = 2

When calculate_minimum_coins(3):
Coins:
1: calculate_minimum_coins(2) = 2 → minimum = 3
3: calculate_minimum_coins(0) = 0 → minimum = 1 (better)
4,5: negative → -1
counter[3] = 1

When calculate_minimum_coins(4):
Coins:
1: calculate_minimum_coins(3) = 1 → minimum = 2
3: calculate_minimum_coins(1) = 1 → minimum = 2
4: calculate_minimum_coins(0) = 0 → minimum = 1 (best)
5: negative → -1
counter[4] = 1

When calculate_minimum_coins(5):
Coins:
1: calculate_minimum_coins(4) = 1 → minimum = 2
3: calculate_minimum_coins(2) = 2 → minimum = 2
4: calculate_minimum_coins(1) = 1 → minimum = 2
5: calculate_minimum_coins(0) = 0 → minimum = 1 (best)
counter[5] = 1

When calculate_minimum_coins(6):
Coins:
1: calculate_minimum_coins(5) = 1 → minimum = 2
3: calculate_minimum_coins(3) = 1 → minimum = 2
4: calculate_minimum_coins(2) = 2 → minimum = 2
5: calculate_minimum_coins(1) = 1 → minimum = 2
counter[6] = 2

When calculate_minimum_coins(7):
Coins:
1: calculate_minimum_coins(6) = 2 → minimum = 3
3: calculate_minimum_coins(4) = 1 → minimum = 2 (better)
4: calculate_minimum_coins(3) = 1 → minimum = 2
5: calculate_minimum_coins(2) = 2 → minimum = 2
counter[7] = 2
Summary:

The memoization table stores the minimum coins needed for each amount from 0 to 7.
This avoids recalculating the same subproblems multiple times.
The final answer for total=7 is 2 coins.
Let me know if you want me to clarify any specific part!
"""
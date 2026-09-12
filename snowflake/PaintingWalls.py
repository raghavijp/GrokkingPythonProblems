from math import inf

def minCostToPaintWalls(cost, time):
    n = len(cost)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[n][i] = inf

    for i in range(n-1, -1, -1):
        for remain in range(1, n+1):
             paint = cost[i] + dp[i+1][max(0, remain - 1 - time[i])]
             dont_paint = dp[i+1][remain]
             dp[i][remain] = min(paint, dont_paint)

    return dp[0][n]

def minCostOptimized(cost, time):
    n = len(cost)
    dp = [0] * (n+1)
    prevDp = [inf] * (n+1)

    for i in range(n-1,-1,-1):
        dp = [0] * (n+1)

        for remain in range(1, n+1):
            paint = cost[i] + prevDp[max(0, remain - 1 - time[i])]
            dont_paint = prevDp[remain]
            dp[remain] = min(paint, dont_paint)

        prevDp = dp

    return dp[n]

def main():
    cost = [1,2,3,2]
    time = [1,2,3,2]

    ans = minCostOptimized(cost, time)

    print(ans)



if __name__ == "__main__":
    main()
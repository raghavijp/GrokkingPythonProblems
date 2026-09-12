def bestTimeToBuyAndSell(profit):
    minPrice = float("inf")
    maxProfit = 0

    for i in range(len(profit)):
        if profit[i] < minPrice:
            minPrice = profit[i]
        elif profit[i] - minPrice > maxProfit:
            maxProfit = profit[i] - minPrice

    return maxProfit

def main():
    nums = [1,2,4,2,5,7,2,4,9,0,9]
    print(f"profit array: {nums}")
    print(f"profit : {bestTimeToBuyAndSell(nums)}")

if __name__ == "__main__":
    main()
from typing import List

def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r != len(prices):
        if prices[l] > prices[r]:
            l = r
            r += 1
        else:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1
    return max_profit


if __name__ == "__main__":
    output = maxProfit([2,1,2,1,0,1,2])
    print(output)
from typing import List


def maxProfit(prices: List[int]) -> int:
    print(prices)
    result = 0
    for i in range(len(prices)-1):
        print(prices[i])
        if prices[i] <= prices[i+1]:
            result += prices[i+1] - prices[i]
    return result
maxProfit([7,1,5,3,6,4])
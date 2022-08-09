# first solution: 저점과 현재 값의 차이 계산
# 시간복잡도: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = prices[0]
        profit = 0
        for price in prices:
            min_stock = min(min_stock, price)
            profit = max(profit, price - min_stock)

        return profit
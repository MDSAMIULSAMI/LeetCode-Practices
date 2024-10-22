class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            # print("Profit:", price, min_price, profit)

            if profit > max_profit:
                max_profit = profit

        return max_profit

test = Solution()

prices = [7,1,5,3,6,4]
print(test.maxProfit(prices))

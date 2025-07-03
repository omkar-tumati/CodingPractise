"""121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution(object):
    def maxProfit(self, prices):
        max_diff = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                difference = prices[j] - prices[i]
                if difference > max_diff:
                    max_diff = difference

        return max_diff
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
    print(sol.maxProfit([2, 4, 1]))           # Output: 2
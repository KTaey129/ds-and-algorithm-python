# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r != len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxP = max(maxP, prof)

            else:
                l = r

            r += 1

        return maxP

# Problem: Given list of numbers, find max profit by buying on any day and selling on a future day
# Solution: Greedy Algorithm, two pointers: for each L, iterate R across and calculate profit, when R is > L, we know we have evaluated all potentila max profits, so move L to where R is and reepat
# O(N) time with left and right pointers single itersation
# O(1) Space

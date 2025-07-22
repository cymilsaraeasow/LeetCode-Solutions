# ✅ Problem: Best Time to Buy and Sell Stock
# 🔗 Link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 🗓️ Date: 2025-07-09
# 🧠 Language: Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for i in prices[1:]:
            if min>i:
                min=i
            profit=max(profit,i-min)
        return profit
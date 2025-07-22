# ✅ Problem:Single Number
# 🔗 Link:https://leetcode.com/problems/single-number/
# 🗓️ Date: 2025-06-24
# 🧠 Language: Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)<2:
                return i
        
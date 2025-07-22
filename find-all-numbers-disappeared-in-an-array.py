# ✅ Problem: Find All Numbers Disappeared in an Array
# 🔗 Link:https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# 🗓️ Date: 2025-06-24
# 🧠 Language: Python
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        full_set = set(range(1, n + 1))
        nums_set = set(nums)
        missing = list(full_set - nums_set)
        return missing
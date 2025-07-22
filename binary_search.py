# ✅ Problem:Binary Search
# 🔗 Link:https://leetcode.com/problems/binary-search/
# 🗓️ Date: 2025-07-22
# 🧠 Language: Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        return -1
        
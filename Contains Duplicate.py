# ✅ Problem: Contains Duplicate
# 🔗 Link: https://leetcode.com/problems/contains-duplicate/description/
# 🗓️ Date: 2025-06-22
# 🧠 Language: Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
     numset=set()
     for i in nums:
        if i in numset:
            return  True
        numset.add(i)
     return False
        
# ✅ Problem:  Remove Duplicates from Sorted Array
# 🔗 Link:https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# 🗓️ Date: 2025-06-28
# 🧠 Language: Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
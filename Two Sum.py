# ✅ Problem: Two Sum
# 🔗 Link:https://leetcode.com/problems/two-sum/
# 🗓️ Date: 2025-06-22
# 🧠 Language: Python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]
        return []
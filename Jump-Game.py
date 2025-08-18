# ✅ Problem:Jump-Game
# 🔗 Link:https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
# 🗓️ Date: 2025-08-18
# 🧠 Language: Python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
       maxreach=0
       last=len(nums)-1
       for i in range(len(nums)):
            if i>maxreach:
                return False
            maxreach=max(maxreach,i+nums[i])
            if maxreach>=last:
                return True
# ✅ Problem:Rotate Array
# 🔗 Link:https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# 🗓️ Date: 2025-08-11
# 🧠 Language: Python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n 
        start, end = 0, n - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        start, end = 0, k - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        start, end = k, n - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
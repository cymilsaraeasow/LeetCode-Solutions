# ✅ Problem: Climbing stairs
# 🔗 Link:https://leetcode.com/problems/climbing-stairs/
# 🗓️ Date: 2025-07-03
# 🧠 Language: Python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second

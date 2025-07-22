# ✅ Problem: Counting-bits
# 🔗 Link:https://leetcode.com/problems/counting-bits/description/
# 🗓️ Date: 2025-07-09
# 🧠 Language: Python
class Solution:
    def countBits(self, n: int) -> List[int]:
        list=[]
        for i in range(n+1):
            a=bin(i)[2:]
            b=a.count('1')
            list.append(b)
        return list

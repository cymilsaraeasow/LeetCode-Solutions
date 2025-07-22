# ✅ Problem:Missing-Number
# 🔗 Link:https://leetcode.com/problems/missing-number/
# 🗓️ Date: 2025-06-24
# 🧠 Language: Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)+1
        total=0
        sum=0
        for i in range(length):
            total+=i
        print('Expected total is ',total)
        for  i in nums:
            sum=sum+i
        print('sum is ',sum)
        miss=total-sum
        return miss
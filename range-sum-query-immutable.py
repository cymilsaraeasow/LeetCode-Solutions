# ✅ Problem:  Range Sum Query - Immutable
# 🔗 Link:https://leetcode.com/problems/range-sum-query-immutable/description/
# 🗓️ Date: 2025-07-07
# 🧠 Language: Python
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        total=0
        for i in nums:
            total+=i
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
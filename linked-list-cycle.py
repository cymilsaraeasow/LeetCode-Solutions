# ✅ Problem:linked-list-cycle
# 🔗 Link:https://leetcode.com/problems/linked-list-cycle/
# 🗓️ Date: 2025-07-09
# 🧠 Language: Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         current=head
         link=set()
         while(current!=None):
             if current not in link:
                 link.add(current)
                 current=current.next
             else:
                 return True
         return False


        
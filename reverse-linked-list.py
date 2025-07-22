# ✅ Problem:reverse-linked-list
# 🔗 Link:https://leetcode.com/problems/reverse-linked-list/description/
# 🗓️ Date: 2025-07-22
# 🧠 Language: Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        previous=None
        while current:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        return previous
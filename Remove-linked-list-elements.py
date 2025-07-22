# ✅ Problem: Remove Linked List Elements
# 🔗 Link:https://leetcode.com/problems/remove-linked-list-elements/description/
# 🗓️ Date: 2025-07-15
# 🧠 Language: Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        current=dummy
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next
       
        
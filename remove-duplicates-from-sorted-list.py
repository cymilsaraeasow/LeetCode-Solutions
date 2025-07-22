# ✅ Problem:remove-duplicates-from-sorted-list
# 🔗 Link:https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 🗓️ Date: 2025-07-18
# 🧠 Language: Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=head
        while head and head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return res
        
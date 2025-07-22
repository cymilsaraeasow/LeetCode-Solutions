# ✅ Problem:Palindrome Linked List
# 🔗 Link:https://leetcode.com/problems/palindrome-linked-list/description/
# 🗓️ Date: 2025-07-15
# 🧠 Language: Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding the middle element in the linked list
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reversing the second half
        prev=None
        while slow:
            next_el=slow.next
            slow.next=prev
            prev=slow
            slow=next_el
        #comparing the first half and second half
        first_half=head
        second_half=prev
        while second_half:
            if first_half.val!=second_half.val:
                return False
            first_half=first_half.next
            second_half=second_half.next
        return True

        
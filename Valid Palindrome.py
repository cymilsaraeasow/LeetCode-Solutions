# ✅ Problem:Valid Palindrome
# 🔗 Link:https://leetcode.com/problems/valid-palindrome/
# 🗓️ Date: 2025-08-20
# 🧠 Language: Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():  # compare case-insensitive
                    return False
                # move both pointers if equal
                left += 1
                right -= 1
                
        return True

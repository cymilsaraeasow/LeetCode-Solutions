# ✅ Problem:valid-Anagram
# 🔗 Link:https://leetcode.com/problems/valid-anagram/
# 🗓️ Date: 2025-06-23
# 🧠 Language: Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

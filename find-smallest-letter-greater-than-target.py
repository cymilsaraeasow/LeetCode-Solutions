# ✅ Problem:find-smallest-letter-greater-than-target
# 🔗 Link:https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 🗓️ Date: 2025-07-22
# 🧠 Language: Python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]
        
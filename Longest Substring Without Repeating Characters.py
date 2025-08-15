# ✅ Problem:Longest Substring Without Repeating Characters
# 🔗 Link:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 🗓️ Date: 2025-08-15
# 🧠 Language: Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        curr=set()
        ans=0
        for right in range(len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left+=1
            curr.add(s[right])
            ans=max(ans,right-left+1)
        return ans
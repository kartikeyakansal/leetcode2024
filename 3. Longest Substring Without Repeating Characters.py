class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = r = 0
        store = [-1] * 128
        for r in range(len(s)):
            if store[ord(s[r])] >= l:
                l = store[ord(s[r])] + 1
            store[ord(s[r])] = r
            ans = max(ans, r - l + 1)
        return ans   
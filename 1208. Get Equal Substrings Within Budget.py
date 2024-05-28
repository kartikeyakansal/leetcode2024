class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = []
        for i in range(n):
            diff.append(abs(ord(s[i]) - ord(t[i])))
        l = r = maxlen = curr = 0
        while curr <= maxCost and r < n:
            curr += diff[r]
            r += 1
            while(curr > maxCost):
                maxlen = max(maxlen, r - l - 1)  
                curr -= diff[l]
                l += 1
        return max(maxlen, r - l)
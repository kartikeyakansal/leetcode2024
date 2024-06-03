class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        s = s.lower()
        s1, s2 = s[:n], s[n:]
        c1 = 0
        for c in s1:
            if c in ['a', 'e', 'i', 'o', 'u']:
                c1 += 1
        for c in s2:
            if c in ['a', 'e', 'i', 'o', 'u']:
                c1 -= 1
        if c1:
            return False
        return True

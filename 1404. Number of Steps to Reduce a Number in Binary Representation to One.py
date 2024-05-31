class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        ans, carry = 0, 0
        for i in range(n - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2:
                ans += 2
                carry = 1
            else:
                ans += 1

        return ans + carry

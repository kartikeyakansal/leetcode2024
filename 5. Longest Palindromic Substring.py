class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = 1
                ans = [i, i+1]
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if (dp[i+1][j-1] and s[i] == s[j]):
                    dp[i][j] = 1
                    ans = [i, j]

        i, j = ans
        return s[i: j + 1]
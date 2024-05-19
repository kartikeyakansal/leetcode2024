class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        index = 0
        step = -1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        ans = ""
        for i in rows:
            ans += i
            
        return ans
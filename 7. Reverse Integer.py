class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag = True if x < 0 else False
        x = abs(x)
        while(x):
            num += (x % 10)
            num *= 10
            x //= 10
        
        num //= 10
        if(num > 2**31 - 1):
            return 0
        else: 
            return -1*num if flag else num
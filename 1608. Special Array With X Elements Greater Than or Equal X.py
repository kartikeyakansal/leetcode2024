class Solution:
    # def specialArray(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     l = 1
    #     r = 100
    #     while(l <= r):
    #         mid = (l + r) // 2
    #         x = 0
    #         for i in range(n):
    #             x += (nums[i] >= mid)
    #         if(x == mid):
    #             return x
    #         if(x > mid):
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return -1

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[min(n, num)] += 1
        number = n
        for i in range(1, n + 1):
            number -= freq[i-1]
            if i == number:
                return i
        return -1
    

    /Users/karti/Desktop/ASU/Summer 2024/Leetcode/leetcode2024/1608. Special Array With X Elements Greater Than or Equal X.py
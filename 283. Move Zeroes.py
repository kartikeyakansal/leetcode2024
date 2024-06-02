class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1

def twoSum(self, nums, target):
    store = {}
    for i in range(len(nums)):
        if nums[i] in store.keys():
            return [i, store[nums[i]]]
        store[target - nums[i]] = i
    return []
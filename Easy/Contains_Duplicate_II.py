class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_index = {}

        for i in range(len(nums)):
            if nums[i] in num_index and i - num_index[nums[i]] <= k:
                return True
            num_index[nums[i]] = i
        return False

nums = [1,2,3,1]
k = 3
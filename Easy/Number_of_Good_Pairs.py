class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter = counter + 1
                    
        return counter
        
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        counter = 0

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    counter = counter + 1

        return counter
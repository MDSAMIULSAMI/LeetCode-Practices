class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        outcome = []
        for i in range(len(nums)):
            if target == nums[i]:
                outcome.append(i)
        return outcome

test = Solution()
nums = [1,2,5,2,3] 
target = 2
print(test.targetIndices(nums, target))
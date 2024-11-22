class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        outcome = []
        for i in range(len(nums)):
            outcome.append(nums[nums[i]])
        return outcome

test = Solution()

nums = [5,0,1,2,3,4]

print(test.buildArray(nums))
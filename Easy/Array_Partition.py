class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        summations = []
        while nums:
            summations.append(min(nums.pop(0), nums.pop(0)))
        return sum(summations)


test  = Solution()
nums = [6,2,6,5,1,2]

print(test.arrayPairSum(nums))
        
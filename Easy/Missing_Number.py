class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
    
test = Solution()
nums = [0, 1, 2]

print(test.missingNumber(nums))
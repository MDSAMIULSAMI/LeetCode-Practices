class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return sum(nums[i:i+3])
            
        return 0
    
test = Solution()

nums = [2,1,2]
print(test.largestPerimeter(nums))

nums = [1, 2, 1, 10]
print(test.largestPerimeter(nums))

nums = [3,6,2,3]
print(test.largestPerimeter(nums))
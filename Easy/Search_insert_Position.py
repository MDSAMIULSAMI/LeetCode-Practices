class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        idx = 0

        if target in nums:
            idx = nums.index(target)
        else:
            for val in nums:
                if val < target:
                    # print(val)
                    idx = nums.index(val)+1
        return idx
    
test = Solution()

nums = [1,3,5,6]
target = 2
print(test.searchInsert(nums, target))

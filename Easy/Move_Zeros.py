class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        print(nums)

nums = [0, 1, 2, 0, 3, 1, 0, 0, 9]

test = Solution()

test.moveZeroes(nums=nums)
print(test.moveZeroes.__doc__)
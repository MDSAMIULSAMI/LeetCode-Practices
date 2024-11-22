class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        arr = []
        i = 0

        while i < len(nums):

            arr.append(nums[i + 1])
            arr.append(nums[i])

            i = i + 2
        return arr


test = Solution()
nums = [2,5]

print(test.numberGame(nums))
        
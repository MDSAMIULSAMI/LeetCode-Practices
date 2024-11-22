class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) // 2

            if mid < len(nums) and nums[mid] == target:
                return mid
            elif mid < len(nums) and nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


test = Solution()

nums = [-1,0,3,5,9,12]
target = 9

print(test.search(nums, target))

nums = [-1,0,3,5,9,12]
target = -13000

print(test.search(nums, target))
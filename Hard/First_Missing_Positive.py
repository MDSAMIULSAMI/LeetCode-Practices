class Solution1:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = 1
        # nums.sort()
        print(nums)
        while True:
            if n in nums:
                n = n + 1
            else:
                break
        return n

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] >= n:
                nums[i] = 0

        #cyclic sort
        for i in range(n):
            while 1 <= nums[i] < n and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, n):
            if nums[i] != i:
                return i
        return n

test = Solution()
nums = [1,2,0]
nums = [3,4,-1,1]
print(test.firstMissingPositive(nums))

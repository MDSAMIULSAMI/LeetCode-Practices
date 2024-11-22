class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

test = Solution()
nums = [0,4,5,0,3,6]

print(test.containsDuplicate(nums))
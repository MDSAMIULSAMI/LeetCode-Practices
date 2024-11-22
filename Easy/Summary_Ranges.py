class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        store = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i = i + 1
                
            if start != nums[i]:
                store.append(f"{start}->{nums[i]}")
            else:
                store.append(f"{nums[i]}")

            i = i + 1
        return store
    
test = Solution()

nums = [0,1,2,4,5,7]

print(test.summaryRanges(nums))
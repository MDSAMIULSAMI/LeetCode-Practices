class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        store = []

        for num in nums:
            if num not in seen:
                seen.add(num)
        
        for i in range(len(nums)):
            if i + 1 not in seen:
                store.append(i+1)

        return store
    
test = Solution()
nums = [1, 1]

print(test.findDisappearedNumbers(nums))
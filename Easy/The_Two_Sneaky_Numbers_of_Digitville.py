class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        freq = {}
        store = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if value > 1:
                store.append(key)

        return store
    
test = Solution()

nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(test.getSneakyNumbers(nums))
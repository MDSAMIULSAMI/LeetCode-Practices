class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        store = []

        for num in nums:
            if num not in store:
                store.append(num)
        # print(store)
        nums.clear()
        nums.extend(store)
        print(nums)

        return len(store)
    
test = Solution()
nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(test.removeDuplicates(nums))





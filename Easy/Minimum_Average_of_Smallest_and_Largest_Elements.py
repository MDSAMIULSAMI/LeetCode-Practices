class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        avg = []
        minE = 0
        maxE = 0

        while True:
            if nums:
                minE = min(nums)
                maxE = max(nums)
                # print(nums, avg)
                nums.remove(minE)
                nums.remove(maxE)
            
                avg.append((maxE+minE)/2)
            else:
                break

        return min(avg)
    
test = Solution()
nums = [1,2,3,7,8,9]

print(test.minimumAverage(nums))
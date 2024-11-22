class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        length = len(nums) // 2
        left = nums[:length]
        right = nums[length:]
        outcome = []

        for i in range(len(left)):
            outcome.append(left[i])
            outcome.append(right[i])
        
        return outcome
    
test  = Solution()

nums = [2,5,1,3,4,7]
n = 3

print(test.shuffle(nums, n))
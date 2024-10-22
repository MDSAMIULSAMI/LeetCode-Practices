from itertools import permutations

class Solution1:
    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) == 2:
            nums[0] , nums[1] = nums[1], nums[0]
            print(nums)
        
        elif len(nums) > 1:
            next_idx = 0
            perm = list(permutations(nums))
            perm.sort()
            print(perm)
            # print(tuple(data))
            for p in perm:
                if p == tuple(nums):
                    # print(perm.index(p))
                    next_idx = perm.index(p) + 1

            while True:
                if next_idx < len(perm):
                    if perm[next_idx] != tuple(nums):
                        break
                    else:
                        next_idx = next_idx + 1
                else:
                    next_idx = 0
                    break

            l = list(perm[next_idx]) 
            nums.clear()

            for val in l:
                nums.append(val)
            print(nums)

        else:
            print(nums)

class Solution2:
    def nextPermutation(self, nums: list[int]) -> None:
        peak_value_indx = nums.index(max(nums)) - 1

        if peak_value_indx == len(nums) - 1:
            nums.sort(reverse=True)
            print(nums)
        
        for idx, value in enumerate(nums[:-peak_value_indx+2]):

                if idx < len(nums[:-peak_value_indx+2]) and value > nums[-peak_value_indx+1]:
                    value , nums[-peak_value_indx+1] = nums[-peak_value_indx+1], value

        nums[peak_value_indx+1:].sort(reverse=True)
        print(nums)

class Solution1:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        for i in range(n, 0, -1):
            if nums[i - 1] < nums[i]:
                next_num_idx = n
                for j in range(n, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        next_num_idx = j
                        break
                nums[i - 1], nums[next_num_idx] = nums[next_num_idx], nums[i - 1]
                nums[i:] = reversed(nums[i:])
                return nums
        return nums.sort()
    
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j =j - 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1

        print(nums) 

test = Solution()
nums = [1,2,3]
test.nextPermutation(nums)

nums = [3,2,1]
test.nextPermutation(nums)

nums = [1,1,5]
test.nextPermutation(nums)

nums = [1,3,2] #[2,1,3]
test.nextPermutation(nums)
# print(nums[-2])
# perm = list(permutations(nums))
# perm.sort()
# print(perm)
# print(tuple(nums))

# for p in perm:
#     if p == tuple(nums):
#         print(perm.index(p))
#         print(perm[perm.index(p)+1])
nums = [1,1]
test.nextPermutation(nums)

nums = [1,2]
test.nextPermutation(nums)

nums = [6,7,5,3,5,6,2,9,1,2,7,0,9]
test.nextPermutation(nums)


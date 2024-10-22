import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums[:] = sorted(nums, reverse=True)
        res = nums[k-1]
        return res

class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]


    
# test = Solution()
test1 = Solution1()

nums = [3,2,1,5,6,4] #[3,2,3,1,2,4,5,5,6]
k = 2
# print("0: ",test.findKthLargest(nums, k))
print("1: ", test1.findKthLargest(nums, k))
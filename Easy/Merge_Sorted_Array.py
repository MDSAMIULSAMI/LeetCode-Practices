class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2[:n])

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3

obj = Solution()
obj.merge(nums1, m, nums2, n)

print(nums1)
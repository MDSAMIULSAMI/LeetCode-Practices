class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        self.nums = nums
        freq = {}

        for value in nums:
            freq[value] = freq.get(value, 0) + 1
            # print(freq)
        for k, v in freq.items():
            if v < 2:
                return k

test = Solution()

set2 = [1, 2, 1, 2, 3]
print(test.singleNumber(set2))
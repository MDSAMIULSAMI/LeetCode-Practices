class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        y = sorted(freq.items(), key=lambda item: (item[1], -item[0]))

        for num, count in y:
            result.extend([num] * count)

        return result 
        

test = Solution()
nums = [1,1,2,2,2,3]

print(test.frequencySort(nums))
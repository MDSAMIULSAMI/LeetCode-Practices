class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        occurs = {}

        for num in nums:
            occurs[num] = occurs.get(num, 0) + 1
        # print(occurs)
        # print("Max:", max(occurs.values()))

        for key, value in occurs.items():
            if value == max(occurs.values()):
                return key
            
class Solution1:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count = count + 1
            else:
                count = count - 1

        return candidate
    
test = Solution()
test2 = Solution1()

s = [2, 2, 1, 1, 4, 1, 4, 4, 4, 4]
print(test.majorityElement(s))
print(test2.majorityElement(s))
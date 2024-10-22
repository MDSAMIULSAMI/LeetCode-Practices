class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                temp = i
                if temp != j and nums[temp] + nums[j] == target:
                    # print(temp, j)
                    if temp not in output:
                        output.append(temp)
                else:
                    temp = temp + 1
        return output
    
test = Solution()

s = [2, 8, 7, 11, 20]
target = 22

print(test.twoSum(s, target))
        
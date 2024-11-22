class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        outcome = []

        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    counter = counter + 1
            outcome.append(counter)

        return outcome




test = Solution()
nums = [6,5,4,8]

print(test.smallerNumbersThanCurrent(nums))
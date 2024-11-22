class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        if sum(arr)%3 != 0:
            return False
        
        eachPart = sum(arr)//3
        currSum, numTimes = 0, 0

        for num in arr:
            currSum = currSum + num
            if currSum == eachPart:
                numTimes = numTimes + 1
                currSum = 0

        return numTimes >= 3


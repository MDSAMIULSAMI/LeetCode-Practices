class Solution:
    def hIndex(self, citations: list[int]) -> int:
        count = 0
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i] > i:
                count =  count + 1
        return count

    
test = Solution()

data = [1,1]
print(test.hIndex(data))
data = [3,0,6,1,5]
print(test.hIndex(data))
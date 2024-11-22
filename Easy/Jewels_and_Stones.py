class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        for i in range(len(stones)):
            if stones[i] in jewels:
                counter = counter + 1
        
        return counter
    

test = Solution()

jewels = "aA"
stones = "aAAbbbb"

print(test.numJewelsInStones(jewels=jewels, stones=stones))

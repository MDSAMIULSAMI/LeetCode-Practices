class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while True:
            if len(stones)>1:
                stones.sort(reverse=True)
                # print(stones)
                # print(stones[0],stones[1]) 
                stones.append(stones[0]-stones[1])
                stones.pop(0)
                stones.pop(0)
            else:
                break

        return stones[0]
    
test = Solution()
# stones = [2,7,4,1,8,1]
stones = [1,3]
# stones = [9,10,1,7,3]
print(test.lastStoneWeight(stones))



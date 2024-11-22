class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and n < 2:
            if flowerbed[0] == 0:
                return True
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                if n > 1:
                    n = n - 1

            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                if n > 1:
                    n = n - 1

            for i in range(1, len(flowerbed)-1):
                if flowerbed[i] != 1:
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        if n > 1:
                            n = n - 1
                        flowerbed[i] = 1

            if n == 0:
                return True
            
        return False
        
test = Solution()

flowerbed = [1,0,0,0,1]
n = 2
print(test.canPlaceFlowers(flowerbed, n)) # false

flowerbed = [1,0,0,0,1]
n = 1
print(test.canPlaceFlowers(flowerbed, n)) #true

flowerbed = [0,0,1,0,1]
n = 1
print(test.canPlaceFlowers(flowerbed, n)) #false

flowerbed = [0,0,1,0,1]
n = 1
print(test.canPlaceFlowers(flowerbed, n)) #true

flowerbed = [1,0,1,0,0]
n = 1
print(test.canPlaceFlowers(flowerbed, n)) #true
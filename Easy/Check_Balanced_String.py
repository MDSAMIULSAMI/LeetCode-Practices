class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_counter = 0
        even_counter = 0
        
        for idx in range(len(num)):
            if idx%2 == 0:
                even_counter = int(num[idx]) + even_counter
            else:
                odd_counter = int(num[idx]) + odd_counter
                
        return even_counter == odd_counter
            
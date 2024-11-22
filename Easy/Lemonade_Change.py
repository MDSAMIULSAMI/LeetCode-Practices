class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0

        for dollar in bills:
            if dollar == 5:
                five = five + 1

            if dollar == 10:
                ten = ten + 1

            change = dollar - 5

            if change == 5:
                if five > 0:
                    five = five - 1
                else:
                    return False
                
            if change == 15:
                if five > 0 and ten > 0:
                    five = five - 1
                    ten = ten - 1
                elif five >= 3:
                    five = five - 3
                else:
                    return False
        return True
    
test = Solution()

bills = [5,5,5,10,20]
print(test.lemonadeChange(bills))
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        seen = []
        max_wealth = []

        for element in accounts:
            summ = 0
            if element not in seen:
                seen.append(element)
                for i in range(len(element)):
                    summ = element[i] + summ
            max_wealth.append(summ)
        
        return max(max_wealth)

test = Solution()

accounts = [[2,8,7],[7,1,3],[1,9,5]]


print(test.maximumWealth(accounts))
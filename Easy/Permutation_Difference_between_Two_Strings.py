class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        outcome = 0
        for i in range(len(s)):
            outcome = abs(s.index(s[i]) - t.index(s[i])) + outcome

        return outcome
    
test = Solution()

s = "abc"
t = "bac"
print(test.findPermutationDifference(s,t))
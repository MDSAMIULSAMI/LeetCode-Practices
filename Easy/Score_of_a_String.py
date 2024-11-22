class Solution:
    def scoreOfString(self, s: str) -> int:
        outcome = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                outcome = abs(ord(s[i]) - ord(s[i+1])) + outcome
                # print(abs(ord(s[i]) - ord(s[i+1])))
        return outcome
    
test = Solution()
s = "hello"
print(test.scoreOfString(s))
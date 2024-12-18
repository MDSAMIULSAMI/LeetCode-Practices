class Solution:
    def makeGood(self, s: str) -> str:
        ans = []

        for c in s:
            if ans and abs(ord(ans[-1]) - ord(c)) == 32:
                ans.pop()
            else:
                ans.append(c)

        return ''.join(ans)
    
test = Solution()
s = "leEeetcode"
print(test.makeGood(s))

s = "abBAcC"
print(test.makeGood(s))
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        print(s+t)
        for char in s + t:
            result = result^ord(char)
        return chr(result)

test = Solution()
s = "abcd"
t = "abcde"
print(test.findTheDifference(s,t))
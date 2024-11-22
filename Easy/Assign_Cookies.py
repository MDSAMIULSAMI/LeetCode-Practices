class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i = 0
        j = 0
        s.sort()
        g.sort()

        while i < len(g) and j < len(s):
                if g[i] <= s[j]:
                    i = i + 1
                j = j + 1

        return i
    
test =  Solution()
g = [1,2,3]
s = [1,1]
print(test.findContentChildren(g,s))

g = [1,2]
s = [1,2,3]
print(test.findContentChildren(g,s))

g = [10,9,8,7]
s = [5,6,7,8]
print(test.findContentChildren(g,s))
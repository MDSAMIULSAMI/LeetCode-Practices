class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq = {}

        for char in s:
            frq[char] = frq.get(char, 0) + 1

        for key, value in frq.items():
            if value == 1:
                return s.find(key)
        return - 1
            
test = Solution()
s = "loveleetcode"
print(test.firstUniqChar(s))

s = "leetcode"
print(test.firstUniqChar(s))

s = "aabb"
print(test.firstUniqChar(s))
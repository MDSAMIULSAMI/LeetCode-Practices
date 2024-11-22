class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        hashmap = {}
        result = ''

        for i in range(len(s)):
            hashmap[indices[i]] = s[i]
        hashmap = sorted(hashmap.items())
        
        for item in hashmap:
            result = result + item[1]

        return result
    
test = Solution()

s = "vttqexwqgdc"
indices = [9,5,8,0,4,3,6,10,1,2,7]
print(test.restoreString(s, indices))
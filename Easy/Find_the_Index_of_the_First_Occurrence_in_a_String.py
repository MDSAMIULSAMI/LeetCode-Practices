class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
test = Solution()

haystack = "ssssabbutsab"
neddle = "sab"
print(test.strStr(haystack, neddle))


class Solution:
    def sortSentence(self, s: str) -> str:
        conv = list(s.split())
        store = []
        result = ''
        for word in conv:
            store.append(word[-1]+word[:-1])
        store.sort()
        
        for item in store:
            result = result + item[1:] +" "
        return result[:-1]
    
test = Solution()

s = "is2 sentence4 This1 a3"
print(test.sortSentence(s))
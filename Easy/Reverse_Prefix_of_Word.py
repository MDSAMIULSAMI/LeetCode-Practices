class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        left = word[:word.index(ch)+1]
        right = word[word.index(ch)+1:]
        wrapper = ''

        for i in range(len(left)-1,-1,-1):
            wrapper = wrapper + word[i]

        return (wrapper+right)
test = Solution()

# word = "abcdefd"
# ch = "d"
word = "abcd"
ch = "z"
print(test.reversePrefix(word, ch))
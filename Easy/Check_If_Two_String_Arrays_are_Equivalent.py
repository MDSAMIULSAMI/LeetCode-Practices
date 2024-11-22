class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        x_1 = ''
        y_1 = ''

        for word in word1:
            x_1 = x_1 + word

        for word in word2:
            y_1 = y_1 + word

        return x_1 == y_1

test = Solution()
word1 = ["ab", "c"]
word2 = ["a", "cb"]

print(test.arrayStringsAreEqual(word1,word2))
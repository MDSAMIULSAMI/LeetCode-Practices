from collections import Counter

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        idx = 1

        while idx < len(words):
            if Counter(words[idx-1]) == Counter(words[idx]):
                words.pop(idx)
            else:
                idx = idx + 1
        return words

test =  Solution()

words = ["abba","baba","bbaa","cd","cd"]
print(test.removeAnagrams(words))

words = ["a","b","c","d","e"]
print(test.removeAnagrams(words))
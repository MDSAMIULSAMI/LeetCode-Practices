class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = set(allowed)
        outcome = len(words)

        for word in words:
            for char in word:
                if char not in allowed:
                    outcome = outcome - 1
                    break #Check for just one mismatch character in word which is not in allowed

        return outcome
    
test = Solution()

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]


print(test.countConsistentStrings(allowed, words))

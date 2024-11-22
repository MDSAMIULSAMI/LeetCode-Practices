class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        acronym = ''
        if len(words) > len(s):
            return False
        else:
            for char in words:
                acronym = acronym + char[0]

            if acronym == s:
                return True
            else:
                return False
            
test = Solution()

words = ["alice","bob","charlie"]
s = "abc"
print(test.isAcronym(words, s))

words = ["an","apple"]
s = "a"
print(test.isAcronym(words, s))

words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
print(test.isAcronym(words, s))
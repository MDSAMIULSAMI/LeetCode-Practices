class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstWord_to_number = ''
        secondWord_to_number = ''
        targetWord_to_number = ''

        for char in firstWord:
            firstWord_to_number = firstWord_to_number + str((ord(char) - 97))
        # print(firstWord_to_number)

        for char in secondWord:
            secondWord_to_number = secondWord_to_number + str((ord(char) - 97))

        # print(secondWord_to_number)

        for char in targetWord:
            targetWord_to_number = targetWord_to_number + str((ord(char) - 97))
        # print(targetWord_to_number)

        return int(firstWord_to_number) + int(secondWord_to_number) == int(targetWord_to_number)


test = Solution()

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

test.isSumEqual(firstWord,secondWord,targetWord)
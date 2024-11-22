class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = list(sentence.split(" "))
        counter = len(sentence)

        if len(sentence) < 2:
            if sentence[0][0] == sentence[0][-1]:
                return True
            else:
                return False
        else:
            if sentence[0][0] == sentence[-1][-1]:
                counter = counter - 1
                for i in range(len(sentence)):
                    if i + 1 < len(sentence) and sentence[i][-1] == sentence[i + 1][0]:
                        counter = counter - 1

            return counter == 0



test = Solution()
sentence = "leetcode exercises sound delightful"
print(test.isCircularSentence(sentence))
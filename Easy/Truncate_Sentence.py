class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x = s.split(" ")
        trun_sent = ''

        for word in x[:k]:
            trun_sent = trun_sent + word + " "

        return trun_sent[:-1]

test = Solution()
s = "Hello how are you Contestant" 
k = 4
print(test.truncateSentence(s,k))
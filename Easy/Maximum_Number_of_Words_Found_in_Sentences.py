class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        for i in range(len(sentences)):
            temp_store = []
            temp_store.append(len(sentences[i].split(" ")))
        return max(temp_store)
    
test = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
sentences = ["please wait", "continue to fight", "continue to win"]
print(test.mostWordsFound(sentences))
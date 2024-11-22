class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        store =[]
        result = []

        for word in words:
            print(word)
            store.append(word.split(separator))

        for items in store:
            for item in items:
                if item != '':
                    result.append(item)
        return result

test = Solution()

words = ["one.two.three","four.five","six"] 
separator = "."
# words = ["$easy$","$problem$"]
# separator = "$"

print(test.splitWordsBySeparator(words, separator))
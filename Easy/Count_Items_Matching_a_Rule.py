class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        # dict_of_items = {}
        result = []
        index = 0

        for item in items:
            dict_of_items = {}
            dict_of_items["type"] = item[0]
            dict_of_items["color"] = item[1]
            dict_of_items["name"] = item[2]
            # print(dict_of_items)
            for key, value in dict_of_items.items():
                if key == ruleKey and value == ruleValue:
                    index = index + 1
                    result.append(index)
        if index != 0:
            return max(result)
        else:
            return 0
test = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(test.countMatches(items, ruleKey, ruleValue))

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

print(test.countMatches(items, ruleKey, ruleValue))

items = [["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"]]
ruleKey = "name"
ruleValue = "qqqq"
print(test.countMatches(items, ruleKey, ruleValue))
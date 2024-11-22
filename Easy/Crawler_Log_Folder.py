class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if "../" in log and stack:
                stack.pop(0)
            else:
                if "./" not in log:
                    stack.insert(0, log)
        # print(stack)
        return len(stack)

test = Solution()

logs = ["d1/","d2/","../","d21/","./"]
print(test.minOperations(logs))

logs = ["d1/","d2/","./","d3/","../","d31/"]
print(test.minOperations(logs))

logs = ["d1/","../","../","../"]
print(test.minOperations(logs))

logs = ["./","ho3/","tl8/"]
print(test.minOperations(logs))
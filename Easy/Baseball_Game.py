class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # stack = []
        result = []

        for op in range(len(operations)):
            if operations[op].isdecimal():
                # print(operations[op])
                result.insert(0, int(operations[op]))

            if operations[op][0] == "-" and operations[op][1:].isdigit():
                # print(operations[op])
                result.insert(0, int(operations[op]))
            if operations[op] == "C":
                result.pop(0)

            if operations[op] == "D":
                result.insert(0, int(result[0])*2)

            if operations[op] == "+":
                result.insert(0, (int(result[0])+int(result[1])))
                              
            # print(result)
        return sum(result)

test = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(test.calPoints(ops))

ops = ["5","2","C","D","+"]

print(test.calPoints(ops))
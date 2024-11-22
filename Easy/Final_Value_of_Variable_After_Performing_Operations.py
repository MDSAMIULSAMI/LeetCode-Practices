class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        outcome = 0

        for op in operations:
            if op == "++X" or op == "X++":
                outcome = outcome + 1

            if op == "--X" or op == "X--":
                outcome = outcome - 1

        return outcome
    
test = Solution()
operations = ["++X","++X","X++"]


print(test.finalValueAfterOperations(operations))

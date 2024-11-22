class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()","o")
        command = command.replace("(al)","al")

        return command
    
test = Solution()

command = "(al)G(al)()()G"

print(test.interpret(command))
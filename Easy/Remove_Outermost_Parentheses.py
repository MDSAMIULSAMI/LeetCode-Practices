class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        count = 0  # To track the depth of parentheses

        for char in s:
            if char == '(':
                if count > 0:  # Don't add the first '(' of the outermost set
                    result.append(char)
                count += 1
            elif char == ')':
                count -= 1
                if count > 0:  # Don't add the last ')' of the outermost set
                    result.append(char)

        return ''.join(result)
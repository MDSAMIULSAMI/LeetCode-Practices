class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        perm = []
        min = 0
        max = len(s)

        for char in s:
            if char == "I":
                perm.append(min)
                min = min + 1
            elif char == "D":
                perm.append(max)
                max = max - 1
        if s[-1] == "I":
            perm.append(min)
        else:
            perm.append(max)

        return perm
    
test = Solution()
s = "IDID"
print(test.diStringMatch(s))

s = "DDI"
print(test.diStringMatch(s))

def oppositeNumber(num):
    return -num

# Example usage:
print(oppositeNumber(5)) # Output: -5
print(oppositeNumber(-7)) # Output: 7

def reverse_number(num):
  # Reverse the number
    reverse = num[::-1]
  # Return the number
    return reverse

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789
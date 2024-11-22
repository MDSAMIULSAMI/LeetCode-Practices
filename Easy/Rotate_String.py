class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = list(s)
        y = list(goal)
        for idx in range(len(x)):
            x.append(x.pop(0))
            if x == y:
                return True
        return False

test = Solution()

s = "abcde"
goal = "cdeab"

# s = "abcde"
# goal = "abced"
print(test.rotateString(s, goal))
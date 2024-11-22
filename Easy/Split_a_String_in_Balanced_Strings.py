class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left_store = []
        right_store = []

        sets = []

        for i in range(len(s)):
            if s[i] == "R":
                right_store.append(s[i])
            if s[i] == "L":
                left_store.append(s[i])

            if len(right_store) == len(left_store):
                sets.append(right_store+left_store)
                right_store.clear()
                left_store.clear()
        return len(sets)

test = Solution()

s = "LLLLRRRR"
print(test.balancedStringSplit(s))
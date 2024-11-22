def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            outcome = isBadVersion(mid)

            if outcome == True:
                right = mid
            if outcome == False:
                left = mid + 1

        return left
            
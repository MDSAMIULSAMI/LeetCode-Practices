def guess(num: int) -> int:
    pass
class Solution:

    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True:
            mid = (left + right) //  2
            outcome =  guess(mid)

            if outcome == 0:
                return mid
            elif outcome == 1:
                left = mid - 1
            elif outcome == -1:
                right = mid + 1
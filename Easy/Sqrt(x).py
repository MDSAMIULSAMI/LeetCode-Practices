class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
                res = mid
            else:
                return mid
            # print(mid)
        return res

test = Solution()

print(test.mySqrt(8))
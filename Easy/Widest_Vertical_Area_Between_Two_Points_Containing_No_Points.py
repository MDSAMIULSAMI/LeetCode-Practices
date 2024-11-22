class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        result = 0

        for i in range(len(points)-1):
            result = max(result, (points[i+1][0] - points[i][0]))

        return result

test =  Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
print(test.maxWidthOfVerticalArea(points))

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(test.maxWidthOfVerticalArea(points))
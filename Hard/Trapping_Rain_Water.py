class Solution:
    def trap(self, height: list[int]) -> int:
        left_wall = 0
        right_wall = 0

        n = len(height)

        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            
            max_left[i] = left_wall
            max_right[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])

        outcome = 0
        for i in range(n):
            capacity = min(max_left[i], max_right[i])
            outcome = outcome + max(0, capacity - height[i]) 

        return outcome
    
test = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(test.trap(height))
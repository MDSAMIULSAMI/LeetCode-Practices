class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        count = 1
        visited = []
        print(nums)

        for num in nums:
            if num not in visited:
                visited.append(num)
                if num + 1 in nums:
                    count = count + 1
                
        # print(visited)
        return count
    
class Solution1:
  def longestConsecutive(self, nums: list[int]) -> int:
    ans = 0
    seen = set(nums)

    for num in nums:
      if num - 1 in seen:
        continue
      length = 0
      while num in seen:
        num += 1
        length += 1
      ans = max(ans, length)

    return ans
  
test = Solution()
data = [100,4,200,1,3,2]
print(test.longestConsecutive(data))

test1 = Solution()
data1 = [0,3,7,2,5,8,4,6,0,1]
print(test1.longestConsecutive(data1))

test2 = Solution1()
data2 = [9,1,4,7,3,-1,0,5,8,-1,6]
print(test2.longestConsecutive(data2))

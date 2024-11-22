class Solution:
    def mergeTwoLists(self, list1: list[int], list2: list[int]) -> list[int]:
        return sorted(list1 + list2)
    
test = Solution()
list1 = [1,2,4] 
list2 = [1,3,4]

print(test.mergeTwoLists(list1,list2))
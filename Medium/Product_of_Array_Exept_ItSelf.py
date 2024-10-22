class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        store_left = [1] * len(nums)
        store_right = [1] * len(nums)
        result = []

        for i in range(1, len(nums)):
            # print(store_left[i - 1] , nums [i - 1])
            store_left[i] = (store_left[i - 1] * nums [i - 1])
        # return store_left
    
        for i in range(len(nums)-2, -1, -1): #range(start, end, steps)
            # print(store_right[i + 1] , nums [i + 1])
            store_right[i] = (store_right[i + 1] * nums [i + 1])
        # return store_right

        for i in range(len(nums)):
            result.append(store_right[i] * store_left[i])

        return result

# class Solution1:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         store = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     store[i] = store[i] * nums[j]
#         return store
    
test = Solution()
# test1 = Solution1()
data = [2, 1, 3, 4]
# print(math.prod(data))
print(test.productExceptSelf(data))
# print(test1.productExceptSelf(data))
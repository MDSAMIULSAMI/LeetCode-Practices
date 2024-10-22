class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec = bin(int(a, 2) + int(b, 2))[2:]
        # print(a, b)
        return str(dec)
    
test = Solution()
a = "11"
b = "1"
print(test.addBinary(a, b))
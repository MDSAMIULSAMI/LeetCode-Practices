class Solution:
    def validPalindrome(self, s: str) -> bool:
        lst = [i for i in s]
        for idx in range(len(lst)):
            temp = lst[idx]
            lst.pop(idx)
            rev = reversed(lst)
            rlst = [i for i in rev]
            if lst == rlst:
                return True
            else:
                lst.insert(idx,temp)
        
        return False
    
test = Solution()

s ='abca'
print(test.validPalindrome(s))

s ='aba'
print(test.validPalindrome(s))

s ='abc'
print(test.validPalindrome(s))
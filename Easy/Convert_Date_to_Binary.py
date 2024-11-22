class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        return f"{bin(int(year))[2:]}-{bin(int(month))[2:]}-{bin(int(day))[2:]}"

test = Solution()
date = "2080-01-29"

print(test.convertDateToBinary(date))
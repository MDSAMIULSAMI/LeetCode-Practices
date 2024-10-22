class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_conv = "".join(map(str, digits))
        str_conv = int(str_conv) + 1
        output = []

        for val in str_conv:
            output.append(val)

        return output
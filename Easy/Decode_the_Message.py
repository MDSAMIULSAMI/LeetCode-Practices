class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashmap = {}
        unique_key = ''
        ordered_alpha = ''
        result = ''

        for char in key:
            if char not in unique_key and char != " ":
                unique_key = unique_key + char
        # print(unique_key)

        for char in range(97,123):
            ordered_alpha = ordered_alpha + chr(char)
        # print(ordered_alpha)

        for i in range(len(ordered_alpha)):
            # print(unique_key[i], ordered_alpha[i])
            hashmap[unique_key[i]] = ordered_alpha[i]

        for char in message:
            for k, val in hashmap.items():
                if char == k:
                    result = result + val

            if char == " ":
                result = result + " "

        return result
    
test = Solution()
# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(".."+test.decodeMessage(key, message)+"...")
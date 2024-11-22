class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        merger = []
        sorted_names = []

        for i in range(len(names)):
            merger.append([heights[i], names[i]])

        merger.sort(reverse=True)
        print(merger)

        for name in merger:
            sorted_names.append(name[1])

        return sorted_names
    
test = Solution()

names = ["Mary","John","Emma"] 
heights = [180,165,170]
print(test.sortPeople(names, heights))
        
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        store = []

        for i in range(len(seats)):
            store.append(abs(seats[i] - students[i]))

        return sum(store)

test = Solution()
seats = [4,1,5,9]
students = [1,3,2,6]


print(test.minMovesToSeat(seats, students))
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        rotations = 0  # Counter to detect when all students refuse the sandwich

        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                # Student takes the sandwich
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0  # Reset rotations since a sandwich was taken
            else:
                # Move student to the end of the line
                students.append(students.pop(0))
                rotations = rotations + 1  # Increase rotations when a sandwich is refused

        return len(students)
    
test = Solution()

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(test.countStudents(students, sandwiches))

students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(test.countStudents(students, sandwiches))

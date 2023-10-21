
Sort Students by CGPA.

Default (GPT-3.5)

User
Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

ChatGPT
Here is a Python implementation of the sort_students function:

python
Copy code
def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
    return students

# Test the function with sample data
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test data
students = [Student("Alice", "A001", 3.9),
            Student("Bob", "B002", 3.6),
            Student("Charlie", "C003", 3.8)]

# Sorting students based on CGPA
sorted_students = sort_students(students)

# Displaying sorted students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
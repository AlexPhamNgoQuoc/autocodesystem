class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)


class GradeManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def add_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                print(f"Grade {grade} added for student {name}!")
                break
        else:
            print(f"Student {name} not found!")

    def calculate_average(self, name):
        for student in self.students:
            if student.name == name:
                average = student.calculate_average()
                print(f"Average grade for student {name}: {average}")
                break
        else:
            print(f"Student {name} not found!")

    def display_all_students(self):
        if len(self.students) == 0:
            print("No students found!")
        else:
            print("List of students:")
            for student in self.students:
                print(student.name)


# Creating an instance of the GradeManagementSystem
grade_system = GradeManagementSystem()

# Adding students
grade_system.add_student("John")
grade_system.add_student("Alice")
grade_system.add_student("Bob")

# Adding grades
grade_system.add_grade("John", 85)
grade_system.add_grade("Alice", 92)
grade_system.add_grade("Bob", 78)
grade_system.add_grade("Bob", 90)  # Adding another grade for Bob

# Calculating averages
grade_system.calculate_average("John")
grade_system.calculate_average("Alice")
grade_system.calculate_average("Bob")

# Displaying all students
grade_system.display_all_students()

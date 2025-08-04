# Parent class
class College:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print(f"College Name: {self.name}")
        print(f"Location: {self.location}")

# Child class
class Student(College):
    def __init__(self, name, location, student_name, course):
        super().__init__(name, location)
        self.student_name = student_name
        self.course = course

    def display_student(self):
        print(f"Student Name: {self.student_name}")
        print(f"Course Enrolled: {self.course}")

# Using the classes
college1 = Student("Global Tech College", "Bengaluru", "Kusuma", "Python Development")
college1.display_info()
college1.display_student()

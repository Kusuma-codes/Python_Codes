class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        print("\n📘 Admission Details")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Grade:", self.grade)

    def is_eligible(self):
        if self.age >= 5:
            print("✅ Admission Status: Eligible")
        else:
            print("❌ Admission Status: Not Eligible (Minimum age is 5)")

# Taking input from user
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter grade applying for (e.g. 1st, 2nd): ")

# Create object
student1 = Student(name, age, grade)

# Display details and eligibility
student1.display_details()
student1.is_eligible()

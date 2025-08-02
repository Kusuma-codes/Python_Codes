class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive number.")

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")


student1 = Student("Kanda", 21)
student1.display()

print("Current Age:", student1.get_age())
student1.set_age(22)
student1.display()

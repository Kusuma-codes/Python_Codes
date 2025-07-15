class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}
    
    def add(self, subject, marks):
        self.subjects[subject] = marks
    
    def average_marks(self):
        if not self.subjects:
            return "No subject added"
        total = sum(self.subjects.values())
        avg = total/len(self.subjects)
        return f"Average marks: {avg}"
    
    
s1 = Student("Kusuma", 22)
s1.add("English", 95)
s1.add("Python",100)
s1.add("Flask", 95)
s1.add("Django", 100)
print(s1.average_marks())
        
        
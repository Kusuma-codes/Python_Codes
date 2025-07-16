class Mother:
    def skills(self):
        print("Mother: Cooking, Caring")

class Father:
    def skills(self):
        print("Father: Driving, Fixing")

class Child(Mother, Father):
    def my_skills(self):
        print("Child: Playing, Learning")
        
        Mother.skills(self)
        Father.skills(self)

me = Child()
me.my_skills()

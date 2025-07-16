# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Create object of Dog
my_dog = Dog()
my_dog.sound()  
my_dog.bark()   

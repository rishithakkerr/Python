class Student:
    def __init__(self, name, age, rollNumber):
        self.name = name
        self.age = age
        self.rollNumber = rollNumber

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Roll Number: ", self.rollNumber)


s1=Student("Rishi", 20, 68)
s1.display()



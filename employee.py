class Employee:
    def __init__(self, name, deignation, employeeID):
        self.name= name
        if name.isdigit():
            raise NameError("Name cannot be numeric")
        self.designation= deignation
        self.employeeID= employeeID
        if employeeID <= 0:
            raise ValueError("Employee ID must be positive")  
    
    def display(self):
        print("Name: ", self.name)
        print("Designation: ", self.designation)
        print("Employee ID: ", self.employeeID)

name=input("Enter Employee Name: ")
designation=input("Enter Employee Designation: ")
employeeID=int(input("Enter Employee ID: "))
    
s1= Employee(name, designation,employeeID)
s1.display()
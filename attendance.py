class Emp:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name= name
        self.attendance=0
        self.mark_attendance()
        self.show_details()
        print("\n")

    def mark_attendance(self):
        self.attendance +=1
        print(f"{self.name} marked present, Total = {self.attendance}")

    def show_details(self):
        print("\n---Employee Details---")
        print("Employee ID:", self.emp_id)
        print("Name:",self.name)
        print("Days Present:", self.attendance)

e1=Emp(21345068,"Rishi Thakker")
  
name= input("Enter student name: ")
rnumber= input("Enter roll number: ")
maths= float(input("Enter marks in Mathematics: "))
science= float(input("Enter marks in Science: "))
english= float(input("Enter marks in English: "))

print("\n--- Student Report Card ---")
print("Name\t\t: ", name)
print("Roll Number\t: ", rnumber)
total= maths + science + english
print("Total Marks\t: ", total)
avg= total / 3
print("Average Marks\t: ", avg)
if avg>=35:
    result = "Pass"
else:
    result = "Fail"

print("Result\t\t: ", result)
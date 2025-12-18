from student_class import Student, Class
from analytics_engine import AttendanceAnalyzer
from attendance_recorder import AttendanceRecorder
from pathlib import Path
import csv

Path("data").mkdir(exist_ok=True)
Path("visuals").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)

STUDENT_FILE = Path("data/students.csv")
ATTENDANCE_FILE = Path("data/attendance_record.csv")    
REPORT_FILE = Path("reports/attendance_report.txt") 

if not STUDENT_FILE.exists():
    with STUDENT_FILE.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "name", "section", "contact", "status"])

if not ATTENDANCE_FILE.exists():
    with ATTENDANCE_FILE.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "date", "status", "late"])

classroom = Class("10-A", "Mathematics", "Mr. Shetty")

students = []

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    section = input("Enter Section: ")
    contact = input("Enter Contact Number: ")

    student = Student(student_id, name, section, contact)
    students.append(student)
    classroom.add_student(student)


for student in students:
    classroom.add_student(student)

with STUDENT_FILE.open("a", newline="") as f:
    writer = csv.writer(f)
    for student in students:
        writer.writerow([student.student_id, 
                         student.name, 
                         student.section, 
                         student.contact, 
                         student.status])
        
print("\n--- Mark Attendance ---")

for student in students:
    status = input(f"Enter attendance for {student.name} (Present/Absent): ")
    late = False

    if status == "Present":
        late_input = input("Late? (yes/no): ").lower()
        late = True if late_input == "yes" else False

    AttendanceRecorder.mark_attendance(student.student_id, status, late)


analyzer = AttendanceAnalyzer()
percentages = analyzer.attendance_percentage()
chronic_absentees = analyzer.chronic_absentees(classroom.threshold)

analyzer.plot_attendance_bar()
analyzer.plot_daily_attendance()

with REPORT_FILE.open("w") as f:
    f.write("Attendance Report\n")
    f.write("=================\n\n")
    f.write("Attendance Percentage:\n")
    for student_id, percentage in percentages.items():
        f.write(f"Student ID: {student_id}, Attendance: {percentage}%\n")
    
    f.write("\nStudents Below Threshold:\n")
    if chronic_absentees:
        for student_id, percentage in chronic_absentees.items():
            f.write(f"Student ID: {student_id}, Attendance: {percentage}%\n")
    else:
        f.write("No students below the threshold.\n")

print("Attendance processing complete. Report generated at 'reports/attendance_report.txt'.")
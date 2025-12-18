import csv
from datetime import datetime

FILE = "data/attendance_record.csv"

class AttendanceRecord:
    def __init__(self, student_id, date, status, late=False):
        self.student_id = student_id
        self.date = date
        self.status = status
        self.late = late

class AttendanceRecorder:
    @staticmethod
    def mark_attendance(student_id, status, late=False):
        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student_id, datetime.now().date(),status,late])
        print(f"Attendance marked for student {student_id} as {status}.")
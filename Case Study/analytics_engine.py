import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import csv

class AttendanceAnalyzer:
    def __init__(self, filepath="data/attendance_record.csv"):
        self.filepath = filepath
        self.attendance_data = self.load_attendance_data()

    def load_attendance_data(self):
        records = []
        with open(self.filepath, "r") as f:
            reader= csv.DictReader(f)
            for row in reader:
                records.append(row)
        return records
    
    def attendance_percentage(self):
        student_days=defaultdict(list)

        for row in self.attendance_data:
            status = 1 if row["status"] == "Present" else 0
            student_days[row["student_id"]].append(status)

        percentages = {}
        for student_id, days in student_days.items():
            arr= np.array(days)
            percent=(np.sum(arr)/len(arr))*100
            percentages[student_id] = round(percent, 2)

        return percentages
    
    def chronic_absentees(self,threshold=75):
        percentages = self.attendance_percentage()
        return{
            sid: pct for sid, pct in percentages.items()
            if pct < threshold
        }
    
    def daily_attendance_summary(self):
        date_map= defaultdict(list)

        for row in self.attendance_data:
            status = 1 if row["status"] == "Present" else 0
            date_map[row["date"]].append(status)

        dates=[]
        totals=[]

        for date,values in date_map.items():
            dates.append(date)
            totals.append(np.sum(np.array(values)))

        return dates, totals
    
    def plot_attendance_bar(self):
        percentages = self.attendance_percentage()
        students = list(percentages.keys())
        values = list(percentages.values())

        plt.bar(students, values)
        plt.title("Student Attendance Percentage")
        plt.xlabel("Student ID")
        plt.ylabel("Attendance %")
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.savefig("attendance_percentage_bar.png")
        plt.close()
    
    def plot_daily_attendance(self):
        dates, totals = self.daily_attendance_summary()

        plt.plot(dates, totals, marker='o')
        plt.title("Daily Attendance Summary")
        plt.xlabel("Date")
        plt.ylabel("Students Present")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("daily_attendance_summary.png")
        plt.close()
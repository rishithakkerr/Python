class Student:
    def __init__(self, student_id, name, section, contact, status="Active"):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.contact = contact
        self.status = status

class Class:
    def __init__(self, class_name, subject, teacher, threshold=75):
        self.class_name = class_name
        self.subject = subject
        self.teacher = teacher
        self.threshold = threshold
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.class_name}.")
        
    def total_students(self):
        return len(self.students)
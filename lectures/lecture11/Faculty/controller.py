from student_view import StudentView
from model import Database

class StudentController:
    def __init__(self, master):
        self.master = master
        self.model = Database()

    def selected_student(self, studentList):
        selections = studentList.curselection()
        print("Student list ",studentList)
        index = selections[0]
        info = studentList.get(index)
        StudentView(self.master, info)

    def students(self):
        return self.model.getStudents()

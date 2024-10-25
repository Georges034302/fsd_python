import tkinter.messagebox as mb
import tkinter as tk
import random as ran

class Student:
    def __init__(self, mark):
        self.name = f'Student-{ran.randint(100,1000):03}'
        self.mark = mark
        self.g = self.grade(mark)

    def grade(self,mark):
        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "Z"
        return grade
    
    def __str__(self) -> str:
        return f'{self.name} : [{self.mark:4} --> {self.g:4}]'
    
students = []
for s in range(0,10):
    students.append(Student(ran.randint(0,101)))


root = tk.Tk()
root.geometry("300x400")
root.title("TKinter ListBox GUI")
root.configure(bg='#607b8d')
root.resizable(False, False)

listVar = tk.Variable(value=students)
studentList = tk.Listbox(root,listvariable=listVar)
studentList.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()

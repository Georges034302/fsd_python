
import tkinter as tk

class NewWindow(tk.Toplevel):
    def __init__(self, master,msg):
        super().__init__(master=master)
        self.title("Confirmation Window")
        self.geometry("300x200")
        label = tk.Label(self, text=msg,fg='#ffc107',
                       font='Helvetica 12 bold', bg='#607b8d')
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" %(x+300,y))
        self.configure(bg='#607b8d')
        self.resizable(False, False)
        label.place(relx=0.5,rely=0.5,anchor='center')


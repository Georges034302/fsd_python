import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
root.title("TKinter GUI")
root.configure(bg='#607b8d')

label = tk.Label(root, text="Name",fg='#ffc107',
                       font='Helvetica 12 bold', bg='#607b8d')
label.grid(row=0,column=0, padx=5, pady=5)

name = tk.Entry(root)
name.grid(column=1, row=0, padx=5, pady=5)

def show():
    showinfo( title="Welcome",message=f'{name.get()}')

button = ttk.Button(root, text="Close", command= lambda: root.quit())
button.grid(column=1, row=1, padx=5, pady=5)

root.mainloop()

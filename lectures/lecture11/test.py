import tkinter.messagebox as mb
import tkinter as tk
from newwindow import NewWindow

root = tk.Tk()
root.geometry("300x200")
root.title("TKinter GUI")
root.configure(bg='#607b8d')
root.resizable(False, False)

box = tk.LabelFrame(root, text='Sign In', bg='#607b8d', fg='white',
                    padx=20, pady=20, font='Helvetica 10 bold')
box.columnconfigure(0, weight=1)
box.columnconfigure(1, weight=3)
box.place(rely=0.5, relx=0.5, anchor='center')

emailLbl = tk.Label(box, text="Email:", justify='left', fg='#ffc107',
                    font='Helvetica 12 bold', bg='#607b8d')
emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

passwordLbl = tk.Label(box, text="Password:", fg='#ffc107',
                       font='Helvetica 12 bold', bg='#607b8d')
passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

emailText = tk.StringVar()
emailField = tk.Entry(box, textvariable=emailText)
emailField.grid(column=1, row=0, padx=5, pady=5)
emailField.focus()

passwordTxt = tk.StringVar()
passwordField = tk.Entry(box, textvariable=passwordTxt, show="*")
passwordField.grid(column=1, row=1, padx=5, pady=5)

cancelBtn = tk.Button(box,text="Cancel",command=lambda: root.quit())
cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

def clear():
    emailField.delete(0,tk.END)
    passwordField.delete(0,tk.END)
    
def login():
    if(emailText.get() == "j.smith@example.com" and passwordTxt.get() == "user123"):
        info = "Correct email and password"
        # mb.showinfo(title="Login Confirmation",message=info)
        NewWindow(root,info)
        clear()
    else:
        info = "Incorrect email or password"
        mb.showerror(title="Login Error",message=info)
        clear()

loginBtn = tk.Button(box,text="Login",command=login)
loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()


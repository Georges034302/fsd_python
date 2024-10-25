
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("TKinter ListBox GUI")
root.configure(bg='#607b8d')
root.resizable(False, False)

cities = ["Beijing","London","Berlin","Chicago","Sydney","Tokyo"]
listVar = tk.Variable(value=cities)
citiesList = tk.Listbox(root,listvariable=listVar)
citiesList.pack(fill=tk.BOTH, expand=True, padx=20, pady=40)

root.mainloop()

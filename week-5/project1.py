import tkinter as tk
from tkinter import messagebox
import pandas as pd

data = pd.read_csv("GIG-logistics.csv")

def check_employee():
    name = name_entry.get().strip().lower()
    dept = dept_entry.get().strip().lower()

    match = data[(data["Name"].str.lower() == name) & (data["Department"].str.lower() == dept)]

    if not match.empty:
        coworkers = data[(data["Department"].str.lower() == dept) & (data["Name"].str.lower() != name)]["Name"].tolist()
        
        message = f"Welcome, {name.title()}!\n\nOther people in {dept.title()}:\n"
        message += "\n".join(coworkers) if coworkers else "You're the only one in this department."
        messagebox.showinfo("Employee Found", message)
    else:
        messagebox.showerror("Not Found", "Sorry, no employee found with that name and department.")

root = tk.Tk()
root.title("Employee Checker")
root.geometry("350x250")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Department:").pack(pady=5)
dept_entry = tk.Entry(root, width=30)
dept_entry.pack()

tk.Button(root, text="Check Employee", command=check_employee).pack(pady=20)

root.mainloop()

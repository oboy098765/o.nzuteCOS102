import tkinter as tk
from tkinter import messagebox as msgbox
import random as rand

def run():
    pass

    
root = tk.Tk()
root.title("Employee Status Checker")
root.geometry("350x250")

tk.Label(root, text = "Full Name: ").pack(pady=15)
name_entry = tk.Entry(root, width = 30)
name_entry.pack()

tk.Button(root, text="Check", command=run).pack(pady = 40)
root.bind('<Return>', run)

root.mainloop()
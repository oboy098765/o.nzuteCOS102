import tkinter as tk
from tkinter import messagebox as msgbox

def submit_choice(event=None):
    selected = location.get()
    weight = int(weight_entry.get())
    
    if selected == "Epe":
        if weight >= 10:
            msgbox.showinfo("Price to pay", "You are to pay N5000.")
        elif weight < 10:
            msgbox.showinfo("Price to pay", "You are to pay N4000.")
        else:
            msgbox.showerror("Error", "I don't know what you put inside this thing!")
    elif selected == "PAU":
        if weight >= 10:
            msgbox.showinfo("Price to pay", "You are to pay N2000.")
        elif weight < 10:
            msgbox.showinfo("Price to pay", "You are to pay N1500.")
        else:
            msgbox.showerror("Error", "I don't know what you put inside this thing!")        
        

root = tk.Tk()
root.title("Delivery Service Charge Checker")
root.geometry("350x250")

location = tk.StringVar(value="")
tk.Label(root, text = "Weight in kg:" ).pack(pady=5)
weight_entry = tk.Entry(root, width = 30)
weight_entry.pack()

tk.Label(root, text = "Location").pack(pady=5)
tk.Radiobutton(root, text="Epe", variable=location, value="Epe").pack(padx = 10, anchor = "w")
tk.Radiobutton(root, text = "PAU", variable = location, value = "PAU").pack(padx = 10, anchor= "w")

tk.Button(root, text="Submit", command = submit_choice).pack(pady = 10)

root.bind('<Return>', submit_choice)


root.mainloop()
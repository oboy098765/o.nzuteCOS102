import tkinter as tk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import time

def display(val):
    window = tk.Toplevel(root)
    window.title("Payment Price")
    window.geometry("200x100")
    
    label_1 = tk.Label(window, text = f"You are to pay N{val}")
    label_1.pack()   


def submit():
    location = location_entry.get().capitalize().title()
    weight = float(weight_entry.get())
    
    if location == "Ibeju-Lekki":
        if weight >= 10.0:
            price = 5000
            display(price)
        elif weight < 10.0:
            price = 3500
            display(price)
        else:
            msg.showerror("Error", "Invalid weight inputted")
    elif location == "Epe":
        if weight >= 10.0:
            price = 10000
            display(price)
        elif weight < 10.0:
            price = 5000
            display(price)
        else:
            msg.showerror("Error", "Invalid weight inputted")
    else:
        msg.showerror("Error", "Location not available!")

root = tk.Tk()
root.title("Simi Services Price Checker")
root.geometry("400x350")

label_1 = tk.Label(root, text="Welcome to Simi Services! \n ")
label_1.pack()
label_2 = tk.Label(root, text="Here, we will check your price to pay! \n\n")
label_2.pack()
location_label = tk.Label(root, text="Location:  \n")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()
weight_label = tk.Label(root, text = " \nWeight (kg):\n ")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()
enter_button = tk.Button(root, text="Enter",  width = 14, command=submit)
enter_button.pack(pady=20)
root.bind('<Return>', lambda event: submit())



root.mainloop()

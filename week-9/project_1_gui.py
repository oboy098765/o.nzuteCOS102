import tkinter as tk
from tkinter import messagebox as msgbox
import random as rand

class Employee:
    Employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali",
                 "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
                 "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]
    
    Present = []
    Tasks = {
        "Loading": [], "Transporting": [], "Reviewing Orders": [], "Customer Service": [], "Delivering Items": []}
    
    def __init__(self, name):
        self.name = name
    
    def refuse_access(self):
        msgbox.showinfo("I'm sorry...", "You are not an employee here.")

    
    def check_employee(self):
        if self.name in Employee.Employees:
            msgbox.showinfo("Welcome!", f"Welcome to work {self.name}! You are present to work today.")
            self.take_attendance()
            self.assign_task()
        else:
            self.refuse_access()
            
    def take_attendance(self):
        Employee.Present.append(self.name)
        
    def assign_task(self):
        random_task = rand.choice(list(Employee.Tasks.keys()))
        Employee.Tasks[random_task].append(self.name)
        msgbox.showinfo("Your Task!", f"{self.name}, you have been assigned to: {random_task}")
        
def run(event=None):
    name_input = name_entry.get()
    emp = Employee(name_input)
    emp.check_employee()
    
def end():
    window = tk.Toplevel(root)
    window.title("Today's Attendance and Task Assignments")
    window.geometry("500x400")

    attendance_label = tk.Label(window, text="📋 Today's Attendance:", font=("Arial", 12, "bold"))
    attendance_label.pack(pady=(10, 5))
    
    if Employee.Present:
        attendance_text = "\n".join(Employee.Present)
    else:
        attendance_text = "No one is marked present today."

    attendance_display = tk.Label(window, text=attendance_text, justify="left")
    attendance_display.pack()

    task_label = tk.Label(window, text="\n🛠️ Task Assignments:", font=("Arial", 12, "bold"))
    task_label.pack(pady=(20, 5))

    task_text = ""
    for task, people in Employee.Tasks.items():
        people_list = ", ".join(people) if people else "No one assigned"
        task_text += f"{task}: {people_list}\n"

    task_display = tk.Label(window, text=task_text, justify="left")
    task_display.pack()

    tk.Button(window, text="Close", command=window.destroy).pack(pady=10)

    
root = tk.Tk()
root.title("Employee Status Checker")
root.geometry("350x300")

tk.Label(root, text="Full Name:").pack(pady=15)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Button(root, text="Check In", command=run).pack(pady=20)
root.bind('<Return>', run)

tk.Button(root, text="Show Daily Report", command=end, bg="lightblue").pack(pady=20)

tk.Button(root, text="Exit Program", command=root.quit, bg="tomato").pack(pady=10)

root.mainloop()

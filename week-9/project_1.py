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
        print(f"I'm sorry, you're not an employee here.")
    
    def check_employee(self):
        if self.name in Employee.Employees:
            print(f"Welcome to work {self.name}!")
            self.take_attendance()
            self.assign_task()
        else:
            self.refuse_access()
            
    def take_attendance(self):
        Employee.Present.append(self.name)
        print(f"{self.name}, you are present for work today!")
        
    def assign_task(self):
        random_task = rand.choice(list(Employee.Tasks.keys()))
        Employee.Tasks[random_task].append(self.name)
        print(f"{self.name}, you have been assigned to: {random_task}.")

while True:
    name_input = input("\nEnter your full name please: ")
    emp = Employee(name_input)
    emp.check_employee()
    
    again = input("\nDo you want to enter another employee? (yes/no): ").strip().lower()
    if again != 'yes':
        break
    
    

print("\nToday's Attendance:")
print(Employee.Present)

print("\nTask Assignments:")
for task, people in Employee.Tasks.items():
    print(f"{task}: {people}")


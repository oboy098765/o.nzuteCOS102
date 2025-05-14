import tkinter as tk
from tkinter import messagebox as msgbox

class Zenith:
    def __init__(self, employee_name, employee_division):
        self.emp_name = employee_name
        self.emp_division = employee_division
    
    def unique_services(self):
        return []
    
    def mutual_services(self):
        return ["Lines of credit", "Investment management and accounts",
                "Insurance"]

class RetailBanking(Zenith):
    def unique_services(self):
        return ["Retirement and education accounts", "Loans and Mortgages",
                "Checking and Saving"] + self.mutual_services()

class GlobalBanking(Zenith):
    def unique_services(self):
        return ["Multi-currency management services and products", 
                "Foreign currency accounts", "Foreign currency credit cards",
                "Transborder advisory services", "Liquidity management"]

class CommercialBanking(Zenith):
    def unique_services(self):
        return ["Advisory services"] + self.mutual_services()


def run(event=None):
    name_input = name_entry.get().title()
    div_input = div_entry.get().title()
    
    # Instantiate appropriate class based on division input
    if div_input == "Retail Banking":
        employee = RetailBanking(name_input, div_input)
    elif div_input == "Global Banking":
        employee = GlobalBanking(name_input, div_input)
    elif div_input == "Commercial Banking":
        employee = CommercialBanking(name_input, div_input)
    else:
        msgbox.showerror("Invalid Division", "There's no such division.")
        return

    services = employee.unique_services()
    service_text = f"Employee: {name_input}\nDivision: {div_input}\n\nServices:\n" + "\n".join(services)
    
    window = tk.Toplevel(root)
    window.title("Division Services")
    window.geometry("500x400")
    
    div_display = tk.Label(window, text=service_text, justify="left", anchor="w")
    div_display.pack(padx=20, pady=20, anchor="w")

root = tk.Tk()
root.title("Zenith Service Displayer")
root.geometry("350x300")

tk.Label(root, text="Name:").pack(pady=10)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Full Division Name:").pack(pady=10)
div_entry = tk.Entry(root, width=30)
div_entry.pack()

tk.Button(root, text="Check Services", command=run).pack(pady=20)
root.bind('<Return>', run)

root.mainloop()

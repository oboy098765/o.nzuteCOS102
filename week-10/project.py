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
        return ["Advisory services"] +self.mutual_services()
    
        
input1 = input("Please, enter your name: ")
input2 = input("What division do you work in?: ").title()

if input2 == "Retail Banking":
    emp = RetailBanking(input1, input2)
    print("The services rendered in this division are:")
    list = emp.unique_services()
    print(list)

elif input2 == "Global Banking":
    emp = GlobalBanking(input1, input2)
    print("The services rendered in this division are:")
    list = emp.unique_services()
    print(list)

        
elif input2 == "Commercial Banking":
    emp = CommercialBanking(input1, input2)
    print("The services rendered in this division are:")
    list = emp.unique_services()
    print(list)


else:
    print("Your input is not a division of our Banking Sector!")

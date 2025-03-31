print("Hello! \nWelcome to Izifin Technology!")
print("This is an Annual Tax Revenue (ATR) calculator.")

exp = input("Please enter your years of experience: ")

while exp.isalpha():
    print("Please enter your years of experience in numbers only: ")
    exp = input()
while exp == "":
    print("You didn't enter any value.\nPlease enter one:")
    exp = input()

print("\n")
age = input("How old are you please? Enter in numbers: ")

while age.isalpha():
    print("Please enter your age in numbers only: ")
    age = input()
while age == "":
    print("You didn't enter any value.\nPlease enter one:")
    age = input()
    
exp = int(exp)
age = int(age)
    
if exp > 25 and age >= 55:
    print("Your Annual Tax Revenue is N5,600,000.")
elif exp > 20 and age >= 45:
    print("Your Annual Tax Revenue is N4,480,000.")
elif exp > 10 and age >= 35:
    print("Your Annual Tax Revenue (ATR) is N1,500,000.")
elif exp < 0:
    print("You're not serious...")
elif age < 0:
    print("You are not yet born!")
elif exp < 10 and age < 35:
    print("Your Annual Tax Revenue (ATR) is N550,000. ")
else:
    print("You do not fall into the category of those possessing ATR")


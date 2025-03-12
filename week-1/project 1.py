# Python simple interest

cont1 = "y"

print("Welcome. This is a simple interest calculator!")
print("")

while cont1 == "y" :
    principle1 = float(input("Enter the principle amount: "))
    print("")
    while principle1 <= 0:
        print("Principle can't be less than or equal to zero: ")
        principle1 = float(input("Please enter the correct principle amount: "))
        print("")

    rate1 = float(input("Enter the interest rate: "))
    print("")
    while rate1 <= 0:
        print("Rate can't be less than or equal to zero: ")
        rate1 = float(input("Please enter the correct rate: "))
        print("")

    time1 = int(input("What is the time?: "))
    print("")
    while time1 <= 0:
        print("The time can't be less than or equal to zero: ")
        time1 = int(input("Please enter the correct time: "))
        print("")
        print("")

    print(f"Your principle is ${principle1:,.2f}")
    print(f"Your rate is {rate1:.2f} percent")
    print(f"Your time of interest is {time1} years")
    print("")
    
    amount1 = principle1 * (1 + (rate1 / 100)*time1)
    print(f"Your amount after {time1:^} years is ${amount1:,.2f}")
    print("")

    print("Thank You")
    print("")
    cont1 = input("Would you like to go again? (y/n): ").lower()
    print("")
    print("----------------------------------------------------------------")






# Python compound interest calculator

cont2 = "y"

print("Welcome. This is a compound interest calculator!")
print("")

while cont2 == "y" :
    principle2 = float(input("Enter the principle amount: "))
    print("")
    while principle2 <= 0:
        print("Principle can't be less than or equal to zero: ")
        principle2 = float(input("Please enter the correct principle amount: "))
        print("")

    rate2 = float(input("Enter the interest rate: "))
    print("")
    while rate2 <= 0:
        print("Rate can't be less than or equal to zero: ")
        rate2 = float(input("Please enter the correct rate: "))
        print("")

    time2 = int(input("How many years has this compounded for?: "))
    print("")
    while time2 <= 0:
        print("The time can't be less than or equal to zero: ")
        time2 = int(input("Please enter the correct time: "))
        print("")
        print("")

    print(f"Your principle is ${principle2:,.2f}")
    print(f"Your rate is {rate2:.2f} percent")
    print(f"Your time of interest is {time2} years")
    print("")

    amount2 = principle2 * pow((1 + rate2/100), time2)
    print(f"Your amount after {time2:^} years is ${amount2:,.2f}")
    print("")

    print("Thank You")
    print("")
    cont2 = input("Would you like to go again? (y/n): ").lower()
    print("")
    print("----------------------------------------------------------------")
    
    
# Python anuity plan calculator

cont3 = "y"

print("Welcome. This is an annuity plan calculator!")
print("")

while cont3 == "y" :
    pmt = float(input("Enter the PMT amount: "))
    print("")
    while pmt <= 0:
        print("PMT can't be less than or equal to zero: ")
        pmt = float(input("Please enter the correct PMT amount: "))
        print("")

    rate3 = float(input("Enter the interest rate: "))
    print("")
    while rate3 <= 0:
        print("Rate can't be less than or equal to zero: ")
        rate2 = float(input("Please enter the correct rate: "))
        print("")
        
    n = float(input("Enter 'n': "))
    print("")
    while n <= 0:
        print("'n' can't be less than or equal to zero: ")
        ratne2 = float(input("Please enter the correct 'n': "))
        print("")

    time3 = int(input("What is time 't'?: "))
    print("")
    while time3 <= 0:
        print("The time can't be less than or equal to zero: ")
        time3 = int(input("Please enter the correct time: "))
        print("")
        print("")

    print(f"Your PMT is ${pmt:,.2f}")
    print(f"Your rate is {rate3:.2f} percent")
    print(f"'n' is {n:.2f}")
    print(f"Your time is {time3} years")
    print("")

    amount3 = pmt *((pow((1+rate3/n),n * time3) - 1) / (rate3/n))
    print(f"Your amount after {time3:^} years is ${amount3:,.2f}")
    print("")

    print("Thank You")
    print("")
    cont3 = input("Would you like to go again? (y/n): ").lower()
    print("")
    print("----------------------------------------------------------------")
    
    
    
    
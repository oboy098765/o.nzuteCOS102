
import time
name1 = input("Enter the first name: ").capitalize()
while name1 == "":
    print("There was no input. Please input a name: ")
    name1 = input()
age1 = input("How old are you?: ")
while age1 == "":
    print("There was no input. Please input your age: ")
    age1 = input()
while age1.isalpha():
    print("Please type numbers, not words: ")
    age1 = input()
print(f"Hello {name1}. You are {age1} years old")
name2 = input("Enter the second name: ").capitalize()
while name2 == "":
    print("There was no input. Please input a name: ")
    name2 = input()
age2 = input("How old are you?: ")
while age2 == "":
    print("There was no input. Please input your age: ")
    age2 = input()
while age2.isalpha():
    print("Please type numbers, not words: ")
    age2 = input()
print(f"Hello {name2}. You are {age2} years old")


print("Swapping......")
print("-----------------------------------")
print("")
time.sleep(1)
print("Successfully swapped")
time.sleep(1)
print(f"Hello {name1}. You are now {age2} years old.")
print(f"Hello {name2}. You are now {age1} years old.")
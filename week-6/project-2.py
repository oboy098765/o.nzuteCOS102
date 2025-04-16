cs_admitted = []
cs_not_admitted = []
mc_admitted = []
mc_not_admitted = []

cont = "yes"
while cont == "yes":
    print()
    name = input("Enter your name please: ").capitalize()
    department = input("Enter your preferred department (Computer Science or Mass Communication) or (c/m): ").capitalize()
    jamb_score = int(input("Enter your JAMB score: "))
    credits = int(input("How many credits do you have in the five key subjects? "))
    interview_passed = input("Did you pass the interview? (yes/no): ").strip().lower()


    student_info = {
        "Name": name,
        "Department": department.title(),
        "JAMB Score": jamb_score,
        "Credits": credits,
        "Interview Passed": interview_passed
    }

    if department == "Computer Science" or department == "C":
        if jamb_score >= 250 and credits >= 5 and interview_passed == "yes":
            print("Congratulations! You have been admitted into Computer Science.")
            cs_admitted.append(student_info)
        else:
            print("Sorry, you were not admitted into Computer Science.")
            cs_not_admitted.append(student_info)
        cont = input("Is there another user entry? (yes/no): \n")

    elif department == "Mass Communication" or department == "M":
        if jamb_score >= 230 and credits >= 5 and interview_passed== "yes":
            print("Congratulations! You have been admitted into Mass Communication.")
            mc_admitted.append(student_info)
        else:
            print("Sorry, you were not admitted into Mass Communication.")
            mc_not_admitted.append(student_info)
        cont = input("Is there another user entry? (yes/no): \n")

    else:
        print("Invalid department choice. Please choose either 'Computer Science' or 'Mass Communication'.")
        cont = input("Is there another user entry? (yes/no): \n")


print("\n--- Admission Summary ---")
print("Computer Science Admitted:")
print()
for students in cs_admitted:
    print (students, end = "\n")
print()
print("Computer Science Not Admitted:")
print()
for students in cs_not_admitted:
    print (students, end = "\n")
print()
print("Mass Communication Admitted:")
print()
for students in mc_admitted:
    print (students, end = "\n")
print()
print("Mass Communication Not Admitted:")
print()
for students in mc_not_admitted:
    print (students, end = "\n")
print()

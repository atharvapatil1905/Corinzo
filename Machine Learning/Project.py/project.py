while True:
    print("""HI , Welcome to the Project
            please enter your choice
           
            1.I Want to See my Result
            2.Done,I would like exit
           
            """)
    choice = int(input("enter your choice from 1 and 2"))
    if choice == 1:

        def calculate_result():
            Name = str(input("Enter your NAME: "))
            print(f"Hello {Name} , Please enter the Following Details")
            Number_of_Subjects = int(input("Enter the number of subjects: "))
            Total_Marks = 0
            for i in range(Number_of_Subjects):
                Marks = int(input("Enter the marks: "))
                Total_Marks += Marks
            AVG = Total_Marks / 100 * Number_of_Subjects
            if AVG > 90:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is O",
                )
            elif AVG > 80 and AVG <= 90:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is A+",
                )
            elif AVG > 70 and AVG <= 80:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is A",
                )
            elif AVG > 60 and AVG <= 70:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is B+",
                )
            elif AVG > 50 and AVG <= 60:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is B",
                )
            elif AVG > 40 and AVG <= 50:
                print(
                    "Congratulations",
                    Name,
                    "your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is C",
                )
            else:
                print(
                    "Your total marks is",
                    Total_Marks,
                    "and your Average is",
                    AVG,
                    "Your Grade is F",
                )
                print("You are failed")
                print("Better luck next time")

        calculate_result()

    elif choice == 2:
        print("Thank you for using the project")
        break
    else:
        print("Invalid choice")
        print("Please enter a valid choice")

    print("Do you want to continue?")
    continue_choice = input("Enter Y for Yes or N for No: ")
    if continue_choice.lower() != "y":
        print("Thank you for using the project")
        break
    else:
        print("Continuing...")
        continue

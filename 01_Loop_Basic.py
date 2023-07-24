Valid = False
while not Valid:
    Error = "Please enter a number that is actually a number"
    try:

        response = float(input("Enter a number: "))

        if response  > 0:
            valid = True

        else:
            print("Please enter a number that is more than zero")
            print()
    except ValueError:
             print(Error)
             print()
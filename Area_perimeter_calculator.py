
# check input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        error = "Please enter something that is more than zero"


        try:

            #ask user to enter a number
            response = float(input(question))

            #checks number is more than zero
            if response > 0:
                return response
                print(error)
                print()


            #Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
                 print(error)
                 print()

#Main routine goes here
print()
print("**** Area Perimeter Calculator ****")
print()

keep_going = ""
while keep_going =="":

    width = num_check("Width: ")
    print(width)
    height = num_check("Height: ")
    print()
    print("Width", width)
    print("Height", height)
    print()
    area = width*height
    perimeter = width*2+height*2
    print()
    print("Area: {:.2f} units".format(area))
    print("Periemter: {:.2f} units".format(perimeter))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")
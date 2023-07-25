
# check input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        error = "Please enter something that is actually a number"

        try:

            #ask user to enter a number
            response = float(input(question))

            #checks number is more than zero
            if response > 0:
                return response

            #Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
                 print(error)
                 print()

#Main routine goes here
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
print("Area: {} units".format(area))
print("Periemter: {} units".format(perimeter))
print()
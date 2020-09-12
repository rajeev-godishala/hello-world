# this program asks the user for the lenght and width of a room
print("This program finds the area of a room")
lenght = float(input("What is the lenght of your room?: "))
width = float(input("What is the width of your room?: "))
unit = input("How do you want to measure your room?: ")
area = lenght * width
print(f"The area of your room is {area} sqaure {unit}")
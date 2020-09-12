print("This program is calculates the area of a triangle using the length of three sides.")
s1 = float(input("What is the length of your first side of your triangle. Please enter here and no letters: "))
s2 = float(input("What is the length of your second side of your triangle. Please enter here and no letters: "))
s3 = float(input("What is the length of your third side of your triangle. Please enter here and no letters: "))
unit = input("What is the measurement you want to measure in? Please enter here: ")
A = (s1 + s2 + s3) / 2
A_rounded = "%.2f" % A
print(f"The area of your triangle using the numbers you entered is {A_rounded} sq. {unit}")
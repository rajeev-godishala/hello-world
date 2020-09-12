print("")
print("This is a basic math calculator")
print("")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
symbol = input("""Enter mathematical operator: 
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for remainder
type round to round a number:  """)
print ("\nMathematical Equation based on your choice is: ")
if symbol == "+":
    print(f"\n {num1} + {num2} = {num1 + num2} ")
elif symbol == "-":
    print(f"\n {num1} - {num2} = {num1 - num2} ")
elif symbol == "*":
    print(f"\n{num1} * {num2} = {num1 * num2} ")
elif symbol == "/":
    print(f"\n{num1} / {num2} = {num1 / num2} ")
elif symbol == "**":
    print(f" {num1} ** {num2} = {num1 ** num2}")
elif symbol == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
elif symbol == "round":
    num = float(input("Which number do you want to round? Please type any number you wish:"))
    rounded_number = round(num)
    print(rounded_number)

else:
    print("Invalid mathematical operator")
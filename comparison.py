print("")
print("This program compares 2 numbers and gives comparison equation")
print("")
num1 = int(input("Enter the first number you want to compare: "))
num2 = int(input("Enter the second number you want to compare: "))
print("Choose One of the Comparison Operators: > , < , =, !=")
oper = input("Enter the comparison operator:")


if oper == ">":
    if (num2 > num1):
        print(f" {num2} > {num1} ")
    elif (num1 > num2):
        print(f" {num1} > {num2} ")
elif oper == "<":
    if (num2 < num1):
        print(f" {num2} < {num1} ")
    elif (num1 < num2):
        print(f" {num1} < {num2} ")
elif oper == "=" and num1 == num2:
    print(f" {num1} = {num2}")
elif oper == "!=" and num1 != num2:
    print(f" {num1} != {num2} ")
else:
    print ("Invalid Comparison option chosen")

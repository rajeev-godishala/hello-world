# This program is supposed to calculate refund given by how many bottles and the size of the bottles
print("""This program is supposed to calculate refund given by how many bottles and 
the size of the bottles""")
how_many_bottles = int(input("How many bottles do you want to recycle: "))
size_of_bottles = float(input("What is the size of the bottles in liters: "))
print("""If the size of your bottle is less than or equal to 1 liter, you will get 
$0.10 for each bottle you recycle.
If the size of your bottle is more than 1 liter, you will get $0.25 for each bottle 
you recycle.""")
print("I will now calculate the refund you get for recycling the bottles")


if size_of_bottles <= 1:
    print(f" You got a refund of ${how_many_bottles * 0.1}.")
if size_of_bottles > 1:
    print(f"You got a refund of ${how_many_bottles * 0.25}.")
print("Thank you for recycling bottles!")
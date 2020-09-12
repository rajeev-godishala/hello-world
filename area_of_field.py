# This program is supposed to convert the area of a field into acres
#
print("""This program is supposed to convert the area of a field into acres
Please answer this in feet and no alphabets or symbols!""")
#
feet_to_acres = 43650
#
# We are asking the user for the lenght and the width
lenght = float(input("What do you want the lenght of your field to be (in feet): "))
width = float(input("What do you want the width of you field to be (in feet): "))
#
# We are now going to use the user input and convert the area to acres.
acres = lenght * width / feet_to_acres
#
print(f"The area of your field is square {acres} acres big.")
acres_rounded = round(acres)
print(f"This is about {acres_rounded} acres")
print("""This program is basically a self - checkout machine. One task it
is supposed to do is to give the least coins it can give back to the user
It is supposed to give pennies, nickels, dimes, quarters, loonies, and toonies""")
coins = int(input("How many cents do you want to pay. "))
if coins < 0:
    print("Invalid number.")
else:
    toonies = coins // 200
    toonies_leftover = coins % 200
    toonies_formatted = "%.0f" % toonies
    print(f"You get {toonies_formatted} toonies")
    loonies = toonies_leftover // 100
    loonies_leftover = toonies_leftover % 100
    loonies_formatted = "%.0f" % loonies
    print(f"You get {loonies_formatted} loonies")
    quarters = loonies_leftover // 25
    quarters_leftover = loonies_leftover % 25
    quarters_formatted = "%.0f" % quarters
    print(f"You get {quarters_formatted} quarters")
    dimes = quarters_leftover // 10
    dimes_leftover = quarters_leftover % 10
    dimes_formatted = "%.0f" % dimes
    print(f"You get {dimes_formatted} dimes.") 
    nickels = dimes_leftover // 5
    nickels_leftover = dimes_leftover % 5
    nickels_formatted = "%.0f" % nickels 
    print(f"You get {nickels_formatted} nickels.")
    pennies = nickels_leftover // 1
    pennies_formatted = "%.0f" % pennies
    print(f"You get {pennies_formatted} pennies.")
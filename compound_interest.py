# This program is supposed to give interest when a person deposited money
# It will calculate for 1, 2, and 3 years. 
print(""" This program is supposed to give interest when a person deposited money
It will calculate for 1, 2, and 3 years.""")
# I will now ask the user for how much he wants to deposit
deposit = float(input("How much money do you want to deposit? "))
# I will now calculate for 1, 2, and 3 years.
first_year = deposit * 0.04 + deposit
first_year_dollar_format = "%.2f" % first_year
print(f"You are going to get ${first_year_dollar_format} next year.")
second_year = first_year * 0.04 + first_year
second_year_dollar_format = "%.2f" % second_year
print(f"You are going to get ${second_year_dollar_format} next next year.")
third_year = second_year * 0.04 + second_year
third_year_dollar_format = "%.2f" % third_year
print(f"You are going to get ${third_year_dollar_format} next next next year.")
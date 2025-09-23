""" 
Cheng Karmen

You are required to create a Python program that asks the user to enter the
monthly usage and then calculates and displays the amount of the bill to be paid
after receiving the discount
"""

monthly_usage = float(input("Enter monthly usage: "))

discount = 0
if (monthly_usage < 50):
    discount = 0
elif (monthly_usage <= 100):
    discount = 0.05
else:
    discount = 0.2

bill = monthly_usage - (monthly_usage * discount)

print(f"Total bill: RM{bill}")
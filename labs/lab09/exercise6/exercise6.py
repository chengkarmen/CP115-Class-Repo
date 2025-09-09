position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here

overtime_rate = 0
if (position == "Manager"):
    overtime_rate = 30
elif (position == "Supervisor"):
    overtime_rate = 20
elif (position == "Staff"):
    overtime_rate = 15
elif (position == "Intern"):
    overtime_rate = 8

base_rate = 0
if (overtime_hours <= 8):
    base_rate = 1.5
else:
    base_rate = 2.0
hour_rate_bonus = 0
if (is_weekend:True):
    hour_rate_bonus = 5

overtime_pay = overtime_hours * overtime_rate

print(overtime_pay)
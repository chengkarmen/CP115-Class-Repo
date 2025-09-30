position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here

# Define base hourly rates
hourly_rate = 0
if position == "Manager":
    hourly_rate = 30
elif position == "Supervisor":
    hourly_rate = 20
elif position == "Staff":
    hourly_rate = 15
elif position == "Intern":
    hourly_rate = 8

if overtime_hours <= 8:
    overtime_rate = hourly_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
else:
    overtime_rate = hourly_rate * 2.0
    overtime_pay = overtime_hours * overtime_rate

# Add weekend bonus if applicable
if is_weekend.lower() == "yes":
    weekend_bonus = overtime_hours * 5
    overtime_pay += weekend_bonus
    
# Total pay is same as overtime pay
total_pay = overtime_pay

print(overtime_pay)
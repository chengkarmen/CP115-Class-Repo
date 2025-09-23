position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here

hourly_rate = 0
if (position == "Manager"):
    hourly_rate = 35
elif (position == "Supervisor"):
    hourly_rate = 25
elif (position == "Staff"):
    hourly_rate = 18

overtime_pay = (hourly_rate * 1.5) * overtime_hours

if (is_weekend == "Yes"):
    weekend_bonus = 5 * overtime_hours 
    overtime_pay = overtime_pay + weekend_bonus
    
total_pay = overtime_pay


print(hourly_rate)
print(overtime_pay)
print(total_pay) 
current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here

consumption = current_reading - previous_reading
rate = 0
water_cost = 0
if (consumption <= 20):
    rate = 0.57
    water_cost = consumption * rate
elif (consumption <= 35):
    rate = 1.03
    water_cost = 11.4 + ((consumption - 20) * rate)
else:
    rate = 1.4
    water_cost = 11.4 + 15.45 + ((consumption - 35) * rate)

additional_charges = 8 + 2
total_bill = water_cost + additional_charges

print(consumption)
print(water_cost)
print(total_bill)
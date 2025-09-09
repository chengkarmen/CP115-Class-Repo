current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here

consumption = float(current_reading + previous_reading)
water_cost = 0
if (consumption <= 20):
    water_cost = consumption * 0.57
elif (consumption <= 35):
    water_cost = 11.4 + ((consumption - 20) * 1.03)
else:
    water_cost = 11.4 + 15.45 + ((consumption -35) * 1.4)

# add service charge and sewerage
total_bill = water_cost + 8 + 2

print(consumption)
print(water_cost)
print(total_bill)
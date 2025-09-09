main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here

price = 0

if (main_course == "Chicken"):
    main_price = 10
elif (main_course == "Beef"):
    main_price = 12
elif (main_course == "Fish"):
    main_price = 11

if (drink == "Soft Drink"):
    drink_price = 2
elif (drink == "Coffee"):
    drink_price = 3

if (dessert == "Ice Cream"):
    dessert_price = 4
elif (dessert == "Cake"):
    dessert_price = 5

total_food_cost = main_price + drink_price + dessert_price
service_charge = total_food_cost * 0.1

final_bill = total_food_cost + service_charge
if (customer_age > 60):
    final_bill = final_bill - (final_bill * 0.15)
elif (customer_age < 18):
    final_bill = final_bill - (final_bill *0.1)

print(f"{final_bill:.2f}")
import random
restaurant_name = "McDonald's"
restaurant_location = "120-120A Jalan Bukit Bintang, 55100, Kuala Lumpur, Malaysia"
menu1 = "McChicken"
menu2 = "Filet o Fish"
menu3 = "Nasi Lemak"

name_upper = restaurant_name.upper()
name_lower = restaurant_name.lower()
location_length = len(restaurant_location)

special_num = random.randint(1,3)
if special_num == 1:
    special = menu1
elif special_num == 2:
    special = menu2
else:
    special = menu3

customer_num = random.randint(100,999)
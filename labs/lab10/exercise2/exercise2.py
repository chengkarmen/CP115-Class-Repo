age = int(input())
accident_count = int(input())

# Your code here

base_premium = 0
if (age < 25):
    base_premium = 2400
elif (age <=50):
    base_premium = 1800
elif (age > 50):
    base_premium = 2000

accident_penalty = 0
if (accident_count == 0):
    accident_penalty = 0
elif (accident_count <= 2):
    accident_penalty = 300
else:
    accident_penalty = 600

premium = base_premium + accident_penalty
discount_amount = 0
if (accident_count == 0):
    discount_amount = int(premium * 0.1)

final_premium = int(premium - discount_amount)

print(base_premium)
print(final_premium)
print(discount_amount)
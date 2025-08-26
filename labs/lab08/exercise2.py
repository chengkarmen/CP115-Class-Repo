main = 25
appetizer = 12
drink = 8
tax = 0.1
delivery_fee = 5

price = (main * 3) + (appetizer * 2) + (drink * 4)
total_bill = price + (price * tax) + delivery_fee

# get amount in whole ringgit without cents
split_bill = int(total_bill // 6)

print(split_bill)
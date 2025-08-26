membership = 120
training_session = 80
locker_rental = 25
towel_service = 15
registration_fee = 50

first_month = membership + (training_session * 6) + locker_rental + towel_service + registration_fee

# after first month (no registration fee)
monthly_cost = first_month - registration_fee
annual_cost = (monthly_cost * 11) + first_month

print(f"first month: {first_month}\nmonthly cost: {monthly_cost}\nannual cost: {annual_cost}")
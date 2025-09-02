employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here

tax_rate = 0
if (tax_status == "Single"):
    if (base_salary >= 5000):
        tax_rate = 22
    else:
        tax_rate = 18
elif (tax_status == "Married"):
    if (base_salary >= 6000):
        tax_rate = 20
    else:
        tax_rate = 15
elif (tax_status == "Head"):
    if (base_salary >= 5500):
        tax_rate = 25
    else:
        tax_rate = 19


deduction = (base_salary * (tax_rate/100)) + (base_salary * 0.11) + (base_salary * 0.005)
net_salary = (base_salary + (overtime_hours * 35)) - deduction

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
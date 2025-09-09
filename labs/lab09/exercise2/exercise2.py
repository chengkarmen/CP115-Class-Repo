employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here

overtime = overtime_hours * 35 
tax_rate = ""
if (tax_status == "Single"):
    if (base_salary >= 5000):
        tax_rate = "22%"
    else:
        tax_rate = "18%"
elif (tax_status == "Married"):
    if (base_salary >= 6000):
        tax_rate = "20%"
    else:
        tax_rate = "15%"
elif (tax_status == "Head"):
    if (base_salary >= 5500):
        tax_rate = "25%"
    else:
        tax_rate = "19%"

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here

tax_rate = ""
income_after_tax = 0
overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay


if (tax_status == "Single"):
    if (total_income >= 5000):
        tax_rate = "22%"
        income_after_tax = total_income - (total_income * 0.22)
    else:
        tax_rate = "18%"
        income_after_tax = total_income - (total_income * 0.18)
elif (tax_status == "Married"):
    if (total_income >= 6000):
        tax_rate = "20%"
        income_after_tax = total_income - (total_income * 0.2)
    else:
        tax_rate = "15%"
        income_after_tax = total_income - (total_income * 0.15)
elif (tax_status == "Head"):
    if (total_income >= 5500):
        tax_rate = "25%"
        income_after_tax = total_income - (total_income * 0.25)
    else:
        tax_rate = "19%"
        income_after_tax = total_income - (total_income * 0.19)

deductions_applied = (income_after_tax * 0.11) + (income_after_tax * 0.005)
net_salary = income_after_tax - deductions_applied

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
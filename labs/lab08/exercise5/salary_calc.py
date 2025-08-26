import employee_data

medical_ins = 50
parking = 30
raw_salary = employee_data.basic_salary + (employee_data.overtime_rate * employee_data.overtime_hours)
deduction = (raw_salary * 0.11) + (raw_salary * 0.05) + (raw_salary * 0.02) + medical_ins + parking
net_salary = raw_salary - deduction

print(f"\tPAYSLIP")
print(f"Gross Salary: RM{raw_salary}")
print(f"Deduction")
print(f"EPF: 11%\nSOCSO: 0.5%\nEIS: 0.2%")
print(f"Medical Insurance: RM{medical_ins}\nParking: RM{parking}")
print(f"Total Deductions: {deduction}")
print(f"Net salary: {net_salary}")


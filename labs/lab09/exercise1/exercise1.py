# Student Classification System
# Get student information
student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

# TODO your code here
classification = ""

if (GPA >= 3.8) and (credit_hours >= 12):
    classification = "Dean's List"
elif (GPA >= 3.5) and (credit_hours >= 12):
    classification = "Honor Roll"

# Display results
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
print(f"Classification: {classification}")
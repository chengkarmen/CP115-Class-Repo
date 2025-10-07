student_gpa = float(input())
total_score = int(input())
number_extracurricular = input()
completed_interview = input()

# TODO: Your code here

admission_status = ""
if (student_gpa >= 3.0) and (total_score >= 1200) and (number_extracurricular != 0) and (completed_interview.lower == "yes"):
    admission_status = "Accepted"

print(admission_status)
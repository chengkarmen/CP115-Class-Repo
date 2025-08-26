test1 = 78
test2 = 85
test3 = 92
test4 = 67
test5 = 88

total_score = test1 + test2 + test3 + test4 + test5
average_score = total_score / 5

# percentage each test contributes to the total score
percentage1 = (test1 / total_score) * 100
percentage2 = (test2 / total_score) * 100
percentage3 = (test3 / total_score) * 100
percentage4 = (test4 / total_score) * 100
percentage5 = (test5 / total_score) * 100

print(f"Test score 1: {test1}/100")
print(f"Test score 2: {test2}/100")
print(f"Test score 3: {test3}/100")
print(f"Test score 4: {test4}/100")
print(f"Test score 5: {test5}/100")
print(f"Total Score: {total_score}/500\nStudent Average: {average_score}")
print(f"percentage each test contributes to the total score:")
print(f"Test 1: {percentage1}")
print(f"Test 2: {percentage2}")
print(f"Test 3: {percentage3}")
print(f"Test 4: {percentage4}")
print(f"Test 5: {percentage5}")
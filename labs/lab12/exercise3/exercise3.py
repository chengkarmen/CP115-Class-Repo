age_input = input()

# TODO: Your code here

age_count = 0
total_age = 0
while age_input != "done":
    total_age += int(age_input)
    age_count += 1
    age_input = input()

average_age = 0
if age_count != 0:
    average_age = total_age / age_count


print(age_count)
print(total_age)
print(f"{average_age:.2f}")

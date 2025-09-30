num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score

final_score = 0
for i in range(1, num_rounds + 1):
    score = float(input())
    if score > 100:
        score = score + (score * 0.2)
    final_score = final_score + score

rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)
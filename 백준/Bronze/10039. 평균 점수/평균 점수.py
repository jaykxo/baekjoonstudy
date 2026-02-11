score = []

for _ in range(5):
    score.append(max(40, int(input())))

print(sum(score) // 5)
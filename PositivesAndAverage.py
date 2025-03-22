sum = 0
count = 0

for i in range(6):
    A = float(input())
    if A > 0.0:
        sum += A
        count += 1

avg = sum / count
print(f"{count} valores positivos")
print(f"{avg:.1f}")
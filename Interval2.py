N = int(input())  # Number of test cases
in_count = 0
out_count = 0

for _ in range(N):
    num = int(input())
    if 10 <= num <= 20:
        in_count += 1
    else:
        out_count += 1

print(f"{in_count} in")
print(f"{out_count} out")

rabbit = 0
rat = 0
frog = 0
total = 0
N = int(input())
for i in range(N):
    quantity, category = map(str, input().split())
    quantity = int(quantity)
    total = total + quantity
    if category == "C":
        rabbit = rabbit + quantity
    elif category == "R":
        rat = rat + quantity
    elif category == "S":
        frog = frog + quantity

per_rabbit = (rabbit / total) * 100
per_rat = (rat / total) * 100
per_frog = (frog / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbit}")
print(f"Total de ratos: {rat}")
print(f"Total de sapos: {frog}")
print(f"Percentual de coelhos: {per_rabbit:.2f} %")
print(f"Percentual de ratos: {per_rat:.2f} %")
print(f"Percentual de sapos: {per_frog:.2f} %")

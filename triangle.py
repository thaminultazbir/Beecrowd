import math
sides = list(map(float, input().split()))

sorted_sides = sorted(sides)

if (sorted_sides[0] + sorted_sides[1]) > sorted_sides[2]:
    peri = sorted_sides[0] + sorted_sides[1] + sorted_sides[2]
    print(f"Perimetro = {peri:.1f}")
else:
    area = ((sides[0] + sides[1]) / 2) * sides[2]
    print(f"Area = {area:.1f}")

sides = list(map(float, input().split()))
sorted_sides = sorted(sides, reverse=True)
A = sorted_sides[0]
B = sorted_sides[1]
C = sorted_sides[2]

if A >= (B + C):
    print(f"NAO FORMA TRIANGULO")
else:
    if (A**2) == ((B**2) + (C**2)):
        print(f"TRIANGULO RETANGULO")
    if (A**2) > ((B**2) + (C**2)):
        print(f"TRIANGULO OBTUSANGULO")
    if (A**2) < ((B**2) + (C**2)):
        print(f"TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print(f"TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B == C):
        print(f"TRIANGULO ISOSCELES")
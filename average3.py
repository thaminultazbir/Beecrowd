x, y = map(float, input().split())

if x == 0.0 and y == 0.0:
    print(f"Origem")
elif (x > 0 or x < 0) and y == 0:
    print(f"Eixo X")
elif x == 0 and (y > 0 or y < 0):
    print(f"Eixo Y")
elif x > 0 and y > 0:
    print(f"Q1")
elif x > 0 and y < 0 :
    print(f"Q4")
elif x < 0 and y < 0:
    print(f"Q3")
elif x < 0 and y > 0:
    print(f"Q2")
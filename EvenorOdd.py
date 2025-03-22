N = int(input())

for i in range(N):
    X = int(input())
    if X == 0:
        print(f"NULL")
    elif X > 0:
        if X % 2 == 0:
            print(f"EVEN POSITIVE")
        else:
            print(f"ODD POSITIVE")

    elif X < 0:
        if X % 2 == 0:
            print(f"EVEN NEGATIVE")
        else:
            print(f"ODD NEGATIVE")
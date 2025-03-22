def Specification(option):
    cases = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    }
    return cases.get(option, "Invalid Option")

A, B = map(int, input().split())

if A == 1:
    print(f"Total: R$ {(Specification(A) * B):.2f}")
elif A == 2:
    print(f"Total: R$ {(Specification(A) * B):.2f}")
elif A == 3:
    print(f"Total: R$ {(Specification(A) * B):.2f}")
elif A == 4:
    print(f"Total: R$ {(Specification(A) * B):.2f}")
elif A == 5:
    print(f"Total: R$ {(Specification(A) * B):.2f}")

A, B = map(int, input().split())

if A > B:
    hours = (24+B) - A
    print(f"O JOGO DUROU {hours} HORA(S)")

elif B > A:
    hours = B - A
    print(f"O JOGO DUROU {hours} HORA(S)")

elif A == B:
    print(f"O JOGO DUROU 24 HORA(S)")
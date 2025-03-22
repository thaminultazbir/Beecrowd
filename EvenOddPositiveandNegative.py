even = 0
odd = 0
positive = 0
negative = 0
for i in range(5):
    # print(i)
    A = int(input())
    if A == 0:
        if (A % 2 == 0):
            even += 1
        elif (A % 2 == 1):
            odd += 1
    elif(A > 0):
        positive += 1
        if (A % 2 == 0):
            even += 1
        elif (A % 2 == 1):
            odd += 1

    elif (A < 0):
        negative += 1
        if (A % 2 == 0):
            even += 1
        elif (A % 2 == 1):
            odd += 1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")
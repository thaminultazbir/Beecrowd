def Destinations(option):
    cases = {
        61: "Brasilia",
        71: "Salvador",
        11: "Sao Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitoria",
        31: "Belo Horizonte"
    }
    return cases.get(option, "DDD nao cadastrado")

A = int(input())
print(f"{Destinations(A)}")

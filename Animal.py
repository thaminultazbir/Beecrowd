data = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

def identify_animal(tipo1, tipo2, tipo3):
    try:
        # Navigate through the dictionary
        animal = data[tipo1][tipo2][tipo3]
        return animal
    except KeyError:
        return "Animal not found"

tipo1 = str(input())
tipo2 = str(input())
tipo3 = str(input())

print(f"{identify_animal(tipo1, tipo2, tipo3)}")

# Read input
X = float(input())

# Check which interval X belongs to
if 0 <= X <= 25:
    print("Intervalo [0,25]")
elif 25 < X <= 50:
    print("Intervalo (25,50]")
elif 50 < X <= 75:
    print("Intervalo (50,75]")
elif 75 < X <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

import math

# Read input values
A, B, C = map(float, input().split())

# Calculate the discriminant (Delta)
delta = (B ** 2) - (4 * A * C)

# Check conditions for a valid solution
if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    # Calculate the two roots
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)

    # Print results with 5 decimal places
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

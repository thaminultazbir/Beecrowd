N = int(input())  # Read input N

for X in range(1, 10001):  # Loop from 1 to 10000
    if X % N == 2:  # Check remainder condition
        print(X)  # Print valid numbers

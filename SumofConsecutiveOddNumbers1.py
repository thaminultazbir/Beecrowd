a = int(input())
b = int(input())

if a > b:
    a, b = b, a

# Calculate the sum of odd numbers between X and Y
sum_odds = 0
for i in range(a + 1, b):
    if i % 2 != 0:  # Check if the number is odd
        sum_odds += i

# Print the result
print(sum_odds)
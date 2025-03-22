max_value = 0  # Stores the highest number
max_position = 0  # Stores the position (1-based index)

for i in range(1, 101):  # Loop from 1 to 100 (1-based index)
    num = int(input())  # Read input number

    if num > max_value:  # Check if the number is the highest so far
        max_value = num
        max_position = i  # Store the 1-based index

# Print the results
print(max_value)
print(max_position)

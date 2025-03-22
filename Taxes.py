
def calculate_tax(income):
    tax = 0

    if income <= 2000.00:
        return "Isento"
    elif income <= 3000.00:
        tax = (income - 2000.00) * 0.08
    elif income <= 4500.00:
        tax = (1000.00 * 0.08) + (income - 3000.00) * 0.18
    else:
        tax = (1000.00 * 0.08) + (1500.00 * 0.18) + (income - 4500.00) * 0.28

    return f"R$ {tax:.2f}"


income = float(input("Enter your income: "))
result = calculate_tax(income)

print(result)

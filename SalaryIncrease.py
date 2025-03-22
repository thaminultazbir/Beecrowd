salary = float(input())

if 0.00 < salary <= 400.00:
    rate = 15
    reajuste = salary * (rate / 100)
    total_salary = reajuste + salary

elif 400.01 <= salary <= 800.00:
    rate = 12
    reajuste = salary * (rate / 100)
    total_salary = reajuste + salary

elif 800.01 <= salary <= 1200.00:
    rate = 10
    reajuste = salary * (rate / 100)
    total_salary = reajuste + salary

elif 1200.01 <= salary <= 2000.00:
    rate = 7
    reajuste = salary * (rate / 100)
    total_salary = reajuste + salary
elif salary > 2000.00:
    rate = 4
    reajuste = salary * (rate / 100)
    total_salary = reajuste + salary

print(f"Novo salario: {total_salary:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {rate} %")
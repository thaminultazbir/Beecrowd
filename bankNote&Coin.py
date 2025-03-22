def bankNoteAndCoin(value):
    notes = [100, 50, 20, 10, 5, 2]
    coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for note in notes:
        count = int(value // note)
        print(f"{count} nota(s) de R$ {note}.00")
        value -= count*note

    value = round(value, 2)

    print("MOEDAS:")

    for coin in coins:
        count = int(value // coin)
        print(f"{count} moeda(s) de R$ {coin:.2f}")
        value -= count * coin
        value = round(value, 2)

amount = float(input())
bankNoteAndCoin(amount)

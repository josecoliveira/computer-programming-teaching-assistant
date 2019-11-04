allL = []
even = []
odds = []

while True:
    n = int(input())

    if n == -1:
        break

    allL.append(n)
    if n % 2 == 0:
        even.append(n)
    else:
        odds.append(n)

print("Conjunto lido:", ", ".join(map(str, allL)))
print("Conjunto dos valores ímpares:", ", ".join(map(str, odds)))
print("Conjunto dos valores pares:", ", ".join(map(str, even)))


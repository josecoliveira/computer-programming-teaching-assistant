amount_grades = []

for i in range(0, 11):
    amount_grades.append(0)

while True:
    n = int(input())
    
    if n == -1:
        break

    amount_grades[n] += 1

s = sum(amount_grades)

print("N\tFA\tFR")
for i in range(0, 11):
    print(f'{i}\t{amount_grades[i]}\t{amount_grades[i]/s}')

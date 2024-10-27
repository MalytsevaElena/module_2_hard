number_ = int(input("Введите число от 3 до 20: "))
parole = []
if number_ % 2 == 0:
    k = number_
else:
    k = number_ + 1
for i in range(1, k // 2):
    a = i
    for j in range(2, number_):
        b = j
        if j == i:
            continue
        if number_ % (i + j) != 0:
            continue
        else:
            a = str(a)
            b = str(b)
            parole.append(a)
            parole.append(b)
print('result:',("".join(parole)))







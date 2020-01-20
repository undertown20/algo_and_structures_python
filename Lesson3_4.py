# 4. Определить, какое число в массиве встречается чаще всего.

from random import random

M = 10
a = [0] * M
for i in range(M):
    a[i] = int(random() * 2)
    print(a[i], end=" ")

count = 0
countFinal = 0
number = 0
for i in range(M):
    for j in range(M):
        if a[i] == a[j]:
            count += 1
        if count > countFinal:
            countFinal = count
            number = a[j]

    count = 0

print("\nЧисло ", number, " повторяется ", countFinal, " раз")

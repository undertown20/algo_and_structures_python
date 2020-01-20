# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random
E = 8
a = [0] * E
for i in range(E):
    a[i] = int(random() * 50)
    print(a[i], end=" ")


max = a[0]
indexMax = 0
for i in range(E):
    if a[i] > max:
        max = a[i]
        indexMax = i

min = a[0]
indexMin = 0
for i in range(E):
    if a[i] < min:
        min = a[i]
        indexMin = i
t = 0
if indexMax < indexMin:
    t = indexMin
    indexMin = indexMax
    indexMax = t
summ = 0
for i in range(indexMin + 1, indexMax):
    summ = summ + a[i]
print("\n", summ)
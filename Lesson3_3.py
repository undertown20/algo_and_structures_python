# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random
T = 15
a = [0] * T
for i in range(T):
    a[i] = int(random() * 17)
    print(a[i], end=" ")


max = a[0]
indexMax = 0
for i in range(T):
    if a[i] > max:
        max = a[i]
        indexMax = i

min = a[0]
indexMin = 0
for i in range(T):
    if a[i] < min:
        min = a[i]
        indexMin = i
a[indexMin], a[indexMax] = a[indexMax], a[indexMin]
print("\n", a)
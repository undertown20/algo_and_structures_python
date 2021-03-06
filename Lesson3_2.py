# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import random

N = 6
a = [0] * N
for i in range(N):
    a[i] = int(random() * 15)
    print(a[i], end=" ")
print("\n")

b = []
for i in range(N):
    if a[i] % 2 == 0:
        b.append(i)
print(b)
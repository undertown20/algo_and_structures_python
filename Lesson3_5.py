# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

H = 10
a = [0] * H
for i in range(H):
    a[i] = int((random() * 20) - 10)
    print(a[i], end=" ")
numberMin = - 1000
for i in range(H):
    if a[i] >= 0:
        continue
    if a[i] > numberMin:
        numberMin = a[i]
print("\n", numberMin)
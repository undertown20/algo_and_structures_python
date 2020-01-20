# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import random
E = 8
a = [0] * E
for i in range(E):
    a[i] = int(random() * 50)
    print(a[i], end=" ")


min1 = a[0]
indexMin1 = 0
for i in range(E):
    if a[i] < min1:
        min1 = a[i]
        indexMin1 = i

min2 = a[0]
indexMin2 = 0
for i in range(E):
    if i == indexMin1:
        continue
    if a[i] <= min2:
        min2 = a[i]
        indexMin2 = i
print("\n",a[indexMin1],a[indexMin2])
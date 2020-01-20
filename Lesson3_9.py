# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    for j in range(M - 1):
        n = int(random() * 10)
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

t1 = 0
for i in range(M):
    t = 1000

    for j in range(N):
       if a[j][i]<=t:
           t = a[j][i]
    if t>t1:
        t1=t

print(a, "\n",t1)
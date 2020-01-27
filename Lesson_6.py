# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
import sys
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
       if a[j][i] <= t:
           t = a[j][i]
    if t > t1:
        t1 = t

print(a, "\n",t1)


sum_size = 0
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(M)
sum_size += sys.getsizeof(N)
sum_size += sys.getsizeof(t1)
sum_size += sys.getsizeof(j)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(b)
sum_size += sys.getsizeof(s)
sum_size += sys.getsizeof(s)

print('Переменные занимают', sum_size)

# python 3.7 x32
# ОС: Windows 10 x64
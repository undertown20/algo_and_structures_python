# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import defaultdict
from collections import deque

signs = '0123456789ABCDEF'
dict = defaultdict(int)
count = 0

for key in signs:
    dict[key] += count
    count += 1

def my_numbers(string):
    s = 0
    number = deque(string)
    number.reverse()
    for i in range(len(number)):
        s += dict[number[i]] * 16 ** i
    return s


def colculate(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in dict:
            if dict[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)

numb1 = my_numbers(input('Введите первое число:\n ').upper())
numb2 = my_numbers(input('Введите второе число:\n ').upper())

print(f'Сумма: {colculate(numb1 + numb2)}')
print(f'Произведение: {colculate(numb1 * numb2)}')




﻿"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
количество монет, которые нужно перевернуть
"""
"""
n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
if x == 0:
    count_zero += 1
else:
    count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
"""

############################################################################################
"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате 
по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""


s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
x = 0
y = 0
for i in range(1000):
    for j in range(1000):
        if x + y == s and x * y == p:
            print(x, y)


###########################################################################################
"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

# n = int(input("Введите контрольное число: "))

# i = 0
# while 2**i <= n:
#     print(2**i, end=' ')
#     i += 1

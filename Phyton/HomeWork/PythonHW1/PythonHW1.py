﻿"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

"""

"""
n = int(input("Введите трёхзначное число N: "))

a = n % 10
n = n // 10
b = n % 10
n = n // 10

print("Результат вычисления суммы чисел N: ",  n + a + b)
        
"""
###############################################################################################
"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок,если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""

"""
S = int(input("Введите общее количество журавликов (число должно быть чётное): "))
print("Петя: ", {S // 4})
print("Катя: ", {S // 2})
print("Серёжа: ", {S // 4})

"""
###################################################################################################

"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

"""

# n = input("Введите номер билета для проверки: ")
# print("Счастливый" if sum(map(ord, n[:3])) == sum(map(ord, n[3:])) else "Нет")

####################################################################################################

"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no

"""
n = int(input("Введите длинну шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Сколько хотите отломить долек? "))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Можно разломить.')
else:
    print('Нельзя разломить')


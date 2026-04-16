# Приведите к целому типу
# print(int(-1.6))
#
# print(9**19 - int(float(9**19)))


# Переменные
# a = 3
# print(a)
#
# name = input('Enter your name')
# print('Hello', name)
#
# a = int(input())
# print(a*2)

# 1.8 Переменные. Стандартный ввод/вывод
# x = int(input())
# h = int(input())
# m = int(input())
#
# print((x+m)//60+h)
# print((x+m)%60)

# Операторы выражения
# a = bool(False)
# b = True
#
# ((a and b) or ((not a) and (not b)))
# task # 1
# a = int(input())
# b = int(input())
# h = int(input())
#
# if a > h:
#     print('Недосып')
# elif b < h:
#     print('Пересып')
# else:
#     print('Это нормально')

# task
# year = int(input())
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('Високосный')
# else:
#     print('Обычный')



# # task 1.12
# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
#
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# print(s)



# # task 1.12.2
# n = int(input())
#
# if (n > -15 and n <= 12) or (n > 14 and n < 17) or (n >= 19):
#     print(True)
# else:
#     print(False)



# # task 1.12.3
# int1 = float(input())
# int2 = float(input())
# operation = input()
#
# if operation == '+':
#     print(int1 + int2)
# elif operation == '-':
#     print(int1 - int2)
# elif operation == '/':
#     if int2 == 0:
#         print("Деление на 0!")
#     else:
#         print(int1 / int2)
# elif operation == '*':
#     print(int1 * int2)
# elif operation == 'mod':
#     if int2 == 0:
#         print("Деление на 0!")
#     else:
#         print(int1 % int2)
# elif operation == 'pow':
#     print(int1 ** int2)
# elif operation == 'div':
#     if int2 == 0:
#         print("Деление на 0!")
#     else:
#         print(int1 // int2)


# # task 1.12.4
# shape = input()
#
# pi = 3.14
#
# s = 0.0
#
# if shape == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# elif shape == "прямоугольник":
#     a = float(input())
#     b = float(input())
#
#     s = a * b
#
# elif shape == "круг":
#     r = float(input())
#
#     s = pi * (r ** 2)
#
# print(s)




# # task 1.12.5
# i1 = int(input())
# i2 = int(input())
# i3 = int(input())
#
# if i1 >= i2 and i1 >= i3:
#     print(i1)
#     if i2 <= i3:
#         print(i2)
#         print(i3)
#     else:
#         print(i3)
#         print(i2)
#
# elif i2 > i1 and i2 > i3:
#     print(i2)
#     if i1 < i3:
#         print(i1)
#         print(i3)
#     else:
#         print(i3)
#         print(i1)
#
# elif i3 > i1 and i3 > i2:
#     print(i3)
#     if i1 < i2:
#         print(i1)
#         print(i2)
#     else:
#         print(i2)
#         print(i1)




# # task 1.12.6
# programmersCount = int(input())
#
# root = "программист"
#
# end1 = "а"
# end2 = "ов"
#
# outString = repr(programmersCount) + " " + root
#
# if programmersCount >= 0 and programmersCount < 21:
#     if programmersCount == 0 or (programmersCount >= 5 and programmersCount <= 20):
#         outString += end2
#     elif programmersCount == 2 or programmersCount == 3 or programmersCount == 4:
#         outString += end1
# else:
#     intToCompare = int(str(programmersCount)[len(str(programmersCount)) - 1])
#     strToCompare = str(programmersCount)[len(str(programmersCount)) - 2]
#     strToCompare += str(programmersCount)[len(str(programmersCount)) - 1]
#
#     if (strToCompare == "11" or strToCompare == "12" or strToCompare == "13" or strToCompare == "14"):
#         outString += end2
#     elif intToCompare == 2 or intToCompare == 3 or intToCompare == 4:
#         outString += end1
#     elif (intToCompare >= 5 and intToCompare <= 9) or intToCompare == 0:
#         outString += end2
#
#
# print(outString)



# # task 1.12.7
sixDigitsNumber = int(input())

lastThreeDigits = sixDigitsNumber % 1000
firstThreeDigits = sixDigitsNumber // 1000

fourth = lastThreeDigits // 100
fifth = lastThreeDigits // 10 % 10
sixth = lastThreeDigits % 10

first = firstThreeDigits // 100
second = firstThreeDigits // 10 % 10
third = firstThreeDigits % 10

firstSum = first + second + third
lastSum = fourth + fifth + sixth

if firstSum == lastSum:
    print("Счастливый")
else:
    print("Обычный")

# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import mylib

mylib.init()

def GetSimpleDivisors():
    '''Метод возвращает список простых множителей'''
    integers = []
    print("Введите число -", end=' ')
    userNum = mylib.Get_Int_Num()
    primeDivisors = [2, 3, 5, 7]
    for i in primeDivisors:
        if userNum % i == 0:
            integers.append(i)
    return integers

print(GetSimpleDivisors())
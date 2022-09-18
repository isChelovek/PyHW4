# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import mylib
mylib.init()
import random

print("Введите размер генерируеммого массива ", end=' ')
lenList     = mylib.Get_Int_Num()
randomList  = [random.randint(0,10) for i in range(lenList)] #Генерируем массив. Пользователю вводить долго да и делал в предыдущих задачах

def withDict(randomList):
    '''
    Если множеством нельзя то тогда можно словарем)
    Сортировка с помощью словаря
    '''
    a = {}
    for i in randomList:
        a[i]=i
    uniqNumber = []
    for i in a:
        uniqNumber.append(i)
    return uniqNumber

print(f'{randomList} -> {withDict(randomList)}')


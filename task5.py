# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

import re
import mylib
mylib.init()

def encrypts_a_string(strNormal):
    '''шифруем сообщение в лист словарей''' # это была ошибка, ну хоть наигрался
    countMap = []
    countMap.append({strNormal[0]:1}) #Инициализация
    count = 0
    for i in range(1, len(strNormal)):
        tempMap = {strNormal[i]:1}
        if  tempMap.keys()  == countMap[count].keys():
            countMap[count][strNormal[i]] = countMap[count][strNormal[i]] + 1
        else:
            count = count + 1
            countMap.append({strNormal[i]:1})
    return countMap

def dict_to_string(mapDict):
    '''словарь прееобразуем в строку'''
    resultStr = ''
    for i in mapDict:
        resultStr = resultStr + str(i[list(i)[0]]) + str(list(i)[0])
    return resultStr

def decoding(line):
    '''Расшифровка RLE кода. Вход строка типа 12A2F. Толька латиница'''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ' #Конечно можно добавить и руский алфавит но лень принцип не изменится. Хотя надо добавить аграничение на ввод
    tempStr = ''
    for i in line:
        if i in alphabet:
            tempStr = tempStr + i + ','
        else:
            tempStr = tempStr + i
    listStr = tempStr.split(',')
    listStr.pop(len(listStr)-1)
    result = ''
    for i in listStr:
        for j in range(int(i[:-1:])):
            result = result + i[len(i)-1::]
    return result

def writeUserStr(path, strCode):
    f = open(path, 'w' ,encoding='utf-8')
    f.write(strCode)
    f.close() 

def readCodeStr():
    f = open('resultCode.txt', 'r' ,encoding='utf-8')
    strCode = f.readline()
    f.close()
    return strCode

strUser = input('Введите строку для шифровки (только латиница) = ')
writeUserStr('firstFile.txt', strUser)               # Записываем изначальную строку
mapCode = encrypts_a_string(strUser)                 # Создаем словарь и кодируем
codeStr = dict_to_string(mapCode)                    # Из словаря делаем строку. Люблю лишнии действия
print(f'Зашифрованное сообщение {codeStr}')
writeUserStr('resultCode.txt', codeStr)              # Записываем код
codeStr = readCodeStr()                              # Читаем код из файла
decodingStr = decoding(codeStr)                      # Перекодируем обратно
print(f'Расшифрованное сообщение {decodingStr}')
writeUserStr('decoding.txt', decodingStr)            # Записываем разкодированное сообщение. Как получилось три файла, а не два я не знаю
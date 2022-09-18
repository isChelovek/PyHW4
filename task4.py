# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


import mylib
mylib.init() 

print("Введите ключ - ", end = '')
offset  = mylib.Get_Int_Num()

dictCode    = {} # Словарь шифровки
translator  = {} # Словарь дешефровки

def GetDictionaries(dictCode, translator):
    '''заполняем два словаря:
        dictCode   - словарь для кодировки
        translator - словарь для дишифровке'''
    count = 0
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in range(len(alphabet)):
        if i + offset > len(alphabet)-1:
            dictCode[alphabet[count]] = alphabet[(i + offset) - len(alphabet)]
            translator[alphabet[(i + offset) - len(alphabet)]] = alphabet[count]
        else:
            dictCode[alphabet[count]] = alphabet[i + offset]
            translator[alphabet[i + offset]] = alphabet[count]
        count = count + 1

def encode_the_message(strNormal, dictCode):
    '''Создаем зашифрованную строку или расшифрованное зависит словаря'''
    strCode = ''
    for i in strNormal:
        strCode = strCode + dictCode[i]
    return strCode

def writeCodeStr(strCode):
    f = open('textCezari.txt', 'w' ,encoding='utf-8')
    print(f'Зашифрованное сообщение {strCode}')
    f.write(strCode)
    f.close()
def readCodeStr():
    f = open('textCezari.txt', 'r' ,encoding='utf-8')
    strCode = f.readline()
    f.close()
    return strCode


GetDictionaries(dictCode, translator)

strNormal = 'абба'
print(f'Исходное сообщение {strNormal}')
writeCodeStr(encode_the_message(strNormal, dictCode))
print(f'Расшифрованное сообщение {encode_the_message(readCodeStr(), translator)}')

#strCode2 = encode_the_message(strCode, translator)








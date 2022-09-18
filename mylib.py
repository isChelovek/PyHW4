def init():
  '''Чистит экран и делает оступ'''  
  from os import system
  system("cls")
  print()

def Get_Int_Num():
    '''Безопасный целочисленный ввод с консоли'''
    while type:
        input_string = input()
        try:
            number_float = int(input_string)
            return number_float
        except ValueError:
            print('Это не число') 
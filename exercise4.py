import os
os.system("cls")

def Get_Number():
      while True:
        input_data = input("Введите число от 1 до 100 : ")
        if not input_data.isnumeric():
         print("Вы ввели не число. Попробуйте снова: ")
        elif not 1 < int(input_data) <101:
          print("Ваше число не диапазоне. Попробуйте снова")
        else:
          break
      return input_data

def Get_Transformation(num):
    print(type(num))
    get_num = num
    binary_num = ''
    for i in range(0, len(num)):
         while num !=0:
            binary_num += str(int(num) % 2)
            num = int(int(num)/2)
    return print(f'Десятичное число {get_num} в двоичной системе: {binary_num[::-1]}\u2082')

Get_Transformation(Get_Number())    
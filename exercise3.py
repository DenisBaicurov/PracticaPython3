import random
import os 
os.system("cls")

def Get_Real_List():
   list_length= random.randint(3,8)   
   get_list=[]
   for i in range(0,list_length):
    fraction_length=random.randint(1,4)
    get_list.append(round (random.randint(0,11)+random.random(),fraction_length))
   print(f'Получили сисок вещественных чисел{get_list}') 
   print('Находим разницу между минимальным и максимальным значением')
   get_min=round (get_list[0]-int(get_list[0]),4)
   get_max=round (get_list[0]-int(get_list[0]),4)
   for i in range(1,len(get_list)):
    if get_min>get_list[i]-int(get_list[i]):
        get_min=round (get_list[i]-int(get_list[i]),4)
    if get_max< get_list[i]-int(get_list[i]):
        get_max=round (get_list[i]-int(get_list[i]),4)
   print(f'Минимальное значение для дробной части - {get_min}')
   print(f'Максимальное значение для дробной части - {get_max}')
   print(f'Разница между ними {round ((get_max-get_min),4)}')     


Get_Real_List()   
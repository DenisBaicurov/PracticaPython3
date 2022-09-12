import random
def Multiplication_Of_Pairs():
     x=random.randint(4,8)
     get_list=[]
     for i in range(0,x+1):
        get_list.append(random.randint(-10,11))
     lower_limit=0
     upper_limit=len(get_list)-1
     conter_cycle=upper_limit+1
     conter_of_paries=0
     print(get_list)
     print('Считаем произведение пар и выводим их на экран')
     while conter_cycle>1:
        multiplication_Of_Pairs=get_list[lower_limit]*get_list[upper_limit]
        conter_of_paries+=1
        print(f'Произведение {conter_of_paries} пары будет {multiplication_Of_Pairs}')
        upper_limit-=1
        lower_limit+=1
        conter_cycle-=2
Multiplication_Of_Pairs()        

        

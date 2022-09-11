import random
def Get_List():
     list_length=random.randrange(3,8)
     get_list=[]
     for i in range(0,list_length):
        get_list.append(random.randrange(-100,101))
     get_sum=0
     print(f'Имеющийся список  {get_list}')
     print('Выводим элементы на нечётных позициях')  
     for i in range(0,len(get_list)) :
        if (i%2!=0):
            get_sum+=get_list[i]
            print(get_list[i]) 
     
     print (f'Сумма элементов на нечётных позициях будет:  {get_sum}')  
Get_List()  
        

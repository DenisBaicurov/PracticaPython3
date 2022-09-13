import os
os.system("cls")

def Get_Number():
      while True:
        input_data = input("Введите целое положительное число от  : ")
        if not input_data.isnumeric():
         print("Вы ввели не число. Попробуйте снова: ")
    
        else:
          break
      return int (input_data)



def Get_Fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def Print_Get_Fibonacci(num):
    fibonacci_list=list(num)
    negafibonacci_list=[]
    for i in range(0,len(fibonacci_list)):
        if i%2!=0:
         negafibonacci_list.append(str(int(fibonacci_list[i])*(-1)))
        else:
         negafibonacci_list.append(str(int(fibonacci_list[i])))  
    negafibonacci_list.reverse()    
    #print (fibonacci_list)
    #print(negafibonacci_list)

    fibonacci_full = negafibonacci_list.copy() + fibonacci_list.copy()
    print(f'Выводим получившийся список фибоначчи для всех индексов   {fibonacci_full}')
Print_Get_Fibonacci(Get_Fibonacci(Get_Number()))    
    







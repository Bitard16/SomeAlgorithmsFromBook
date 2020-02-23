



def fib(n,tab=0):
    if n ==0:
        return 0
    if n ==1:
        return 1
    return fib(n-1,tab+1) + fib(n-2,tab+1)


print(fib(7))


memo = dict() # Создаем словарь для запоминания полученных до этого значений

def fib_mem(n,tab=0):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        if (n-1,n-2) not in memo:
            memo[(n-1,n-2)] = fib_mem(n-1,tab+1)+ fib_mem(n-2,tab+1)
    return memo[(n-1,n-2)]


print(fib_mem(10,tab=0))


print(memo) # А вот и сам словарь 

from functools import lru_cache


@lru_cache(maxsize = None) #  Декоратор который ускоряет работу программы так как использует кеш для ускорения этой задачи(мемоизация)
def fib(n,tab=0):
    if n ==0:
        return 0
    if n ==1:
        return 1
    return fib(n-1,tab+1) + fib(n-2,tab+1)



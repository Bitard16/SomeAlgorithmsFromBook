# Hash таблицы - часто поиск забирает O(1) времени и старается искать примерное положение ключа(значения) я чейки которое нам нужно
from hashlib import  md5 , sha1
data = [22,40,102,105,23,31,6,5]

hash_table = [None] *15
tbllen = len(hash_table)

def hash_function(value,table_size):
    return value % table_size

for value in data:
    hash_table[hash_function(value,tbllen)] = value

print(hash_table)

def hash_f(element,i,lenght):
    """Функция для создания множетсва хещ-функция"""
    h1 = int(md5(element.encode('ascii')).hexdigest(),16)
    h2 = int(sha1(element.encode('ascii')).hexdigest(),16)
    return (h1+i*h2) %lenght

print (hash_f("CAT",1,10**5))


print (hash_f("CAT",2,10**5))

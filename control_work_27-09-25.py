# Блох Роман ИИ-71 Уровень C
# Задача 1
import numpy
array=[1,6,9,5,3,8]
result = numpy.var(array)
print("Дисперсия:",result,"Среднее арифметическое:",sum(array)/len(array))

# Задача 2
import math
letters_count=int(input("Размер словаря: "))
letters_count_in_row =int(input("Символов в строке: "))
rows=int(input("Строк: "))
print(((round(math.sqrt(letters_count))*letters_count_in_row))*rows*2)

# Задача 3
day=int(input("День: "))
month=int(input("Месяц: "))
year=int(input("Год: "))
if month<=12:
    if month%2!=0:
        if day>31 and month<=7:
            print("Не существует")
        elif day>30 and month>7:
            print("Не существует")
    elif month%2==0:
        if day>30 and month<=7:
            print("Не существует")
        elif day>31 and month>7:
            print("Не существует")
    elif month==2:
        if day>28 and year%4!=0:
            print("Не существует")
        elif day>29 and year%4==0:
            print("Не существует")
    elif month==8:
        if day>31:
            print("Не существует")
else: print("Не существует")




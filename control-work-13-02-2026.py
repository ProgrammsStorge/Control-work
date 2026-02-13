import random
import psutil
import time
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def benchmark(func): # Тест
    def wrapper(*args, **kwargs):
        global number_of_calls
        start_time = time.process_time()
        result = func(*args, **kwargs)
        end_time = time.process_time()
        memory = psutil.Process().memory_info().rss / 1024 ** 2
        print(f"--- Результаты: {func.__name__} ---")
        print(f"Память: {memory:.2f} МБ")
        print(f"Время: {end_time - start_time:.8f} сек")

        return result
    return wrapper


# Первая задача
@benchmark
def bubble_sort_benchmark(lst): # Пызырёк
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
@benchmark
def sort(lst): return  sorted(lst)
rnd_arr=[random.randint(0,100)for i in range(10)] #Генератор списка
print("Пузырьковая сортировка:",bubble_sort_benchmark(rnd_arr))
print("Встроеная сортировка:",sort(rnd_arr))

# Вторая задача

n=int(input())
matrix=[[random.randint(0,10)for j in range(n)]for i in range(n)] #Генератор списка
print("Изначальная матрица")
print_matrix(matrix) # Вывод изначального матрица

x=int(input("Сколько сдвинуть по x: "))
y=int(input("Сколько сдвинуть по y: "))

if y!=0: matrix= matrix[::-1][:y]+matrix[:-y]
if x!=0:
    for i in range(len(matrix)): matrix[i] = matrix[i][::-1][:x] + matrix[i][:-x] # Сдвиг через срезы 
print("Сдвинутая матрица")
print_matrix(matrix)
# Третья задача

def quick_sort(arr): 
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    midl = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + midl +quick_sort(right)

n=int(input())
matrix=[[random.randint(0,10)for j in range(n)]for i in range(n)] # Генератор списка
print("Неотсортированая матрица")
print_matrix(matrix)
matrix=[[matrix[j][i]for j in range(len(matrix[0]))]for i in range(len(matrix))] # Поворот
for i,arr in enumerate(matrix):
    matrix[i]=quick_sort(arr)
print("Отсортированая матрица")
matrix=[[matrix[j][i]for j in range(len(matrix[0]))]for i in range(len(matrix))] # Поворот
print_matrix(matrix)

# Четвёртая задача

@benchmark
def insertion_sort(to_sort):
    sort_list=[]
    j=0
    for i in to_sort:
        for j in range(0,len(to_sort)-1):
            if to_sort[j]>+i:
                break
        sort_list.insert(j,i)
    return sort_list

arr=[random.randint(0,100)for i in range(10)] # Генератор списка
print("Список:",arr)
print("Максимум вставкой:",insertion_sort(arr)[-1])
print("Максимум пузырком:",bubble_sort_benchmark(arr)[-1])

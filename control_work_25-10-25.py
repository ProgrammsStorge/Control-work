import math
import random

# Блох Роман ИП-71
#################################### Задача 1

while True:
    try:
        w_m = int(input("Укажите ширину ширину нижний части треугольника: "))
        h_m = int(input("Укажите высоту треугольника от верхушки до низа: "))
        break
    except ValueError:
        print("Это должно быть целое число!")

full_char=""

while len(full_char)!=1:
    full_char=input("Символ для заполнения: ")
    if len(full_char)!=1:
        print("Символ заполнения должен быть ОДИН!")

main_char="*"
matrix = [[f"{full_char}"for i in range(h_m)] for j in range(w_m)]

def set_pix(xy, sim=main_char):
    global matrix, main_char, anim
    try:
        if xy[0] >= 0 and xy[1] >= 0:
            matrix[round(xy[1])][round(xy[0])] = sim
    except:
        pass  # скорее всего пиксель вышел за экран


def draw_line(point1,point2):
        global matrix
        pointer=point1
        angle = -math.atan2(point2[0] - point1[0], point2[1] - point1[1])
        while True:
            pointer[1] = pointer[1] + (0.1 * math.cos(angle))
            pointer[0] = pointer[0] + (-0.1 * math.sin(angle))
            set_pix(pointer)
            if round(pointer[0]) == round(point2[0]) and round(pointer[1]) == round(point2[1]):
                break


for line in [
        [[5, 0], [10, 10]],
        [[10, 10], [0, 10]],
        [[0, 10], [5, 0]]
    ]:
    point1 = line[0]
    point2 = line[1]
    point1[0] *= (w_m-1) / 10
    point2[1] *= (h_m-1) / 10
    point1[1] *=(h_m-1) / 10
    point2[0] *= (w_m-1) / 10
    draw_line(point1, point2)
for row in matrix:
    for element in row:
        print(element, end='')
    print()

#################################### Задача 2

while True:
    try:
        a_interval = int(input("Минимальное значение промежутка: "))
        b_interval = int(input("Максимальное значение промежутка: "))
        number = int(input("Проверить входит ли это чисто в промежуток: "))
        break
    except ValueError:
        print("Это должно быть целое число!")

interval=[int(i)for i in range(a_interval,b_interval+1)]
print(f"Число {number}",
      "входит" * int(number in interval) +
      "не входит" * int(not number in interval))

#################################### Задача 3

while True:
    try:
        w_m = int(input("Укажите ширину матрицы: "))
        h_m = int(input("Укажите высоту матрицы: "))
        break
    except ValueError:
        print("Это должно быть целое число!")

matrix = [[random.randint(0,9)for i in range(h_m)] for j in range(w_m)]

print("Без сдвига")

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

print("\nС сдвигом")

for row in matrix:
    save=row[0]
    row.pop(0)
    row.append(save)

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

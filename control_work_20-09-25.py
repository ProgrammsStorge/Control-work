# Уровень C
# Блох Роман

# Задача 1
kb = 8
print(f"{kb} Kb - {kb/1024} Mb, {kb*1024} - Bytes, {kb*1024*8} - Bits")

# Задача 2
import math
letters_count=32
letters_count_in_row =112
rows=64
print(((round(math.sqrt(letters_count))*letters_count_in_row))*rows*2)

# Задача 3
temperature=int(input("Градусов в цельсиях: "))
weaters ={"дождь":"Нужно взять зонт.",
          "гроза":"Лучше останься дома.",
          "град":"Возми зонтик или останься дома.",
          "потоп":"Возьмите предметы для плаванья.",
          "ясно":""}
for text in weaters:print(text)
wether = input("Погода: ")
if temperature>=-50 and temperature<=-10:
    print("Оденьтесь очень тепло. Например: куртку, шапку и тёплые штаны.",end=" ")
if temperature >= -9 and temperature <= -0:
        print("Оденьтесь по теплее. Например: лёгенькую куртку, шапку и штаны.", end=" ")
if temperature >= 1 and temperature <= 15:
        print("Оденьтесь несильно жарко. Например: кофту, джинсы.", end=" ")
if temperature >=16  and temperature <= 50:
        print("Оденьтесь легко. Например: майку, шорты.", end=" ")
if wether.lower() in weaters:
    print(weaters[wether.lower()])

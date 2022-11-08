# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 201 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) * Подумайте как наделить бота ""интеллектом""


pleer1 = input('Имя первого игрока - ')
pleer2 = input('Имя второго игрока - ')
from random import randint
hod = randint(1, 2)
if hod == 1:
    one = pleer1
    two = pleer2 
    win = one
    print(f'{pleer1} ходит первым')
else:
   one = pleer2
   two = pleer1 
   win = one
   print(f'{one} ходит первым')

sweets = 201
max = 28
def p1(sweets):
    count1 = 0
    count2 = 0
    while sweets != 0:
        hod1 = sweets % (max + 1)        
        count1 = count1 + hod1  
        print(f'Количество конфет, которые взял {win}: {hod1}')    
        sweets = sweets - hod1         
        print(f'Конфет осталось: {sweets}')
        print(f'У {win} конфет: {count1}') 
        if sweets > 0:
            hod2 = int(input(f'Второй игрок вводит количество конфет: '))   
            count2 = count2 + hod2  
            print(f'У второго игрока конфет: {count2}')   
            sweets = sweets - hod2
            print(f'Конфет осталось: {sweets}')
    return sweets, count1, count2                   
p1(sweets)
print(f'Первый игрок взял конфеты последним, он стал победителем!')


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


s = 'abbcccdddd'
print(f'Исходная строка - {s}\n')
def rle_code(k): 
    coded = ''
    i = 0
    while i < len(k):
        count = 1 
        while i + 1 < len(k) and k[i] == k[i + 1]:
            count += 1
            i += 1 
        coded += str(count) + k[i]
        i += 1 
    return coded

def rle_decode(d):
    decoded = ''
    count = 0
    for el in d:
        if el.isdigit():
           count = int(el)
        else:
            decoded += el * count
            count = 0
    return decoded

s_coded = rle_code(s)
print(f'Сжатая строка = {s_coded}')

s_decoded = rle_decode(s_coded)
print(f'Восстановленная строка - {s_decoded}\n')

with open('s.txt', 'w') as f:   
    f.write(str(s_coded))
with open('s.txt') as file:
    s_cod = file.read() 
print(f'Сжатая строка, считанная из файла - {s_cod}')

with open('s_dec.txt', 'w') as f:   
    f.write(str(s_decoded))

with open('s_dec.txt') as file:
    s_dec = file.read() 
print(f'Восстановленная строка, считанная из файла - {s_dec}\n')


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
 
 
def enter_initial_data():
    player1 = input('Введите имя Первого игрока\n')
    player2 = 'Bot'
    print(f' Вы играете против {player2}')
    total_number=input('Введите общее число конфет -> ')
    max_number=input('Введите max число, которое можно взять за раз -> ')
    lot=rd(0,1)
    if lot==1: 
        print(f'Первый ход у игрока {player1}')
        flag=1
        n=0
    else:
        print(f'Первый ход у игрока {player2}')
        flag=-1
        n=1
    dictionary={'1':player1, '-1':player2, 'flag': flag, 'n':n, 'total_number':total_number, 'max_number':max_number}  
    

    #for item in dictionary:
    #    print('{}:{}'.format(item,dictionary[item])) 
    return dictionary

def game_play():
    initial_data=enter_initial_data()
    while int(initial_data['total_number']) > 0: # условие продалжения игры
        initial_data['flag']=(-1)**initial_data['n'] 
        item=str(initial_data['flag'])
        if int(initial_data['total_number']) <= int(initial_data['max_number']):
            print('Победитель {}'.format(initial_data[item]))
            break
        if int(initial_data['total_number'])>int(initial_data['max_number']): # количество конфет больше мин остатка
           if int(item) == 1:
                a=int(input(f' {initial_data[item]} Введите количество изымаемых конфет-> '))
                initial_data['total_number']=int(initial_data['total_number'])-a
                print('Остаток {}'. format(initial_data['total_number']))
           elif int(item) == -1:
                a=rd(0,int(initial_data['max_number']))
                print(f' {initial_data[item]} выбрал  {a}  изымаемых конфет')
                initial_data['total_number']=int(initial_data['total_number'])-a
                print('Остаток {}'. format(initial_data['total_number'])) 
              
        initial_data['n']+=1
        

from random import randint as rd

game_play()
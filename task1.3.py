# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
 
 
def enter_initial_data3():
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
    dictionary={'1':player1, '-1':player2, 'n':n, 'total_number':total_number, 'max_number':max_number}  
    

    #for item in dictionary:
    #    print('{}:{}'.format(item,dictionary[item])) 
    return dictionary

def game_play3():
    initial_data=enter_initial_data3()
    while int(initial_data['total_number']) > 0: # условие продалжения игры
        item=str((-1)**initial_data['n'] )
        if int(initial_data['total_number']) <= int(initial_data['max_number']):
            print('Победитель {}'.format(initial_data[item]))
            break
        if int(initial_data['total_number'])>int(initial_data['max_number']): # количество конфет больше мин остатка
           if int(item) == 1:
                a=int(input(f' {initial_data[item]} Введите количество изымаемых конфет-> '))
                initial_data['total_number']=int(initial_data['total_number'])-a
                print('Остаток {}'. format(initial_data['total_number']))
           elif int(item) == -1:
                a=ii_bot(initial_data)
                print(f' {initial_data[item]} выбрал  {a}  изымаемых конфет')
                initial_data['total_number']=int(initial_data['total_number'])-a
                print('Остаток {}'. format(initial_data['total_number'])) 
              
        initial_data['n']+=1

def ii_bot(data): 
    a_ii=int(data['total_number'])%(int(data['max_number'])+1)
    if a_ii==0:
        a_ii=rd(1,int(data['max_number']))
    return a_ii   

from random import randint as rd

game_play3()
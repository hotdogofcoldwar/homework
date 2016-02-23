# -*- coding: utf-8 -*-

from __future__ import division

# homework #2 by Khalikov Murad

import sys
import random

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

print(u'''            Игра Пятнашки на заданном размере игрового поля.

            Для победы необходимо расставить все фишки по порядку,
            пустая ячейка должна при этом находиться внизу справа.

            Для движения пустой ячейки используются клавиши w,a,s,d.
            w - двигает пустую ячейку вверх,
            s - двигает ее вниз,
            a - движение влево,
            d - движение вправо

            ''')

# input field size
while True:
    try:
        row_number = input_function(u'Введите желаемое количество столбцов игрового поля в Пятнашках  ')
        line_number = input_function(u'Введите желаемое количество рядов игрового поля в Пятнашках  ')
        field = random.sample(range(int(row_number) * int(line_number)),int(row_number) * int(line_number)) # creates random field list
        break
    except ValueError:
        print(u'Вы ввели не то, что нужно! Попробуйте целые числа ')

empty_mark='empty'

# substitutes 0 to 'empty'
b=int(field.index(0))
field.pop(b)
field.insert(b,empty_mark)

#victory condition
victory=list(range(1,int(line_number)*int(row_number),1))
victory.append(empty_mark)

#functional block
def show_field():
    # show current game field pattern
    i = 0
    while i < int(line_number):
        i += 1
        print(field[(i - 1)*int(row_number):(i * int(row_number))])

def turn_w():
    # w turn pattern
    try:
        global b
        if b - int(row_number) >= 0:
            field[b], field[b - int(row_number)] = field[b - int(row_number)], field[b]
            b=b-int(row_number)
            show_field()
        else:
            print(u'''Вы не можете совершить данный ход
            ''')
    except IndexError:
        print(u''' Вы нажали не ту клавишу
         ''')

def turn_s():
    # s turn pattern
    try:
        global b
        if int(b)+int(row_number) <= int(row_number) * int(line_number)-1:
            field[b], field[b+int(row_number)]=field [b + int(row_number)], field[b]
            b = b + int(row_number)
            show_field()
        else:
            print(u'''Вы не можете совершить данный ход
             ''')
    except IndexError:
        print(u'''
        Вы нажали не ту клавишу ''')

def turn_a():
    # a turn pattern
    try:
        global b
        if int(b) % (int(row_number)) > 0:
            field[b], field[b - 1] = field[b - 1], field[b]
            b= b - 1
            show_field()
        else:
            print(u''' Вы не можете совершить данный ход
             ''')
    except IndexError:
        print(u''' Вы нажали не ту клавишу
         ''')

def turn_d():
    # d turn pattern
    try:
        global b
        if (b + 1) % int(row_number) > 0:
            field[b], field[b+1] = field[b+1], field[b]
            b = b + 1
            show_field()
        else:
            print(u''' Вы не можете совершить данный ход
             ''')
    except IndexError:
        print(u''' Вы нажали не ту клавишу
         ''')

def turn_input():
    # enter your turn pattern
    turn = str(input_function(u''' Введите ваш ход! (w s a d)
    '''))
    if turn == str('w'):
        turn_w()
    elif turn == str('a'):
        turn_a()
    elif turn == str('s'):
        turn_s()
    elif turn == str('d'):
        turn_d()
    else:
        print(u''' Вы нажали не ту клавишу
        ''')

show_field()

while field != victory: #game cycle
    turn_input()

print(u'''
      Ура, победа!''')

# -*- coding: utf-8 -*-

from __future__ import division

# homework #2 by Khalikov Murad

import sys
import random

if sys.version_info[0] == 2:
    input_func = raw_input
else:
    input_func = input

print('''
          ~~~~~~~~~~~~Game of 15 on desired field size~~~~~~~~~~~~

              For victory one should sort the tiles in order
              from the top left corner to right line by line
            Empty tile should be placed in lower right corner.

                    To move empty tile use keys: w,a,s,d.
                     w - moves the empty tile up,
                     s - moves the empty tile down,
                     a - moves the empty tile left,
                     d - moves the empty tile right
            ''')

#  rules and input field size:
while True:
    try:
        row_number = int(input_func('Enter the number of rows on field  '))
        line_number = int(input_func('Enter the number of lines on field  '))

        # creates random field list:
        field = random.sample(range(row_number * line_number),
                              row_number * line_number)
        break
    except ValueError:
        print('Integer number, please! ')

empty_mark = 'empty'
count = 0


# substitutes 0 to 'empty':
b = int(field.index(0))
field.pop(b)
field.insert(b, empty_mark)


# victory condition:
victory = list(range(1, line_number * row_number, 1))
victory.append(empty_mark)


# functional block:
def show_field():
    # show current game field pattern - divides list in row and lines
    i = 0
    while i < line_number:
        i += 1
        print(field[(i - 1) * row_number:(i * row_number)])


def turn_w():
    # w (up) turn pattern
    try:
        global b, count
        if b - row_number >= 0:
            field[b], field[b - row_number] = field[b - row_number], field[b]
            b -= row_number
            count += 1
            show_field()
        else:
            print('''You can't move the tile this direction
                  ''')
    except IndexError:
        print(''' You have pressed wrong key
              ''')


def turn_s():
    # s (down) turn pattern
    try:
        global b, count
        if b + row_number <= row_number * line_number - 1:
            field[b], field[b + row_number] = field[b + row_number], field[b]
            b += row_number
            count += 1
            show_field()
        else:
            print('''You can't move the tile this direction
                  ''')
    except IndexError:
        print(''' You have pressed wrong key
              ''')


def turn_a():
    # a (left) turn pattern
    try:
        global b, count
        if b % row_number > 0:
            field[b], field[b - 1] = field[b - 1], field[b]
            b -= 1
            count += 1
            show_field()
        else:
            print('''You can't move the tile this direction
                  ''')
    except IndexError:
        print(''' You have pressed wrong key
               ''')


def turn_d():
    # d (right) turn pattern
    try:
        global b, count
        if (b + 1) % row_number > 0:
            field[b], field[b + 1] = field[b + 1], field[b]
            b += 1
            count += 1
            show_field()
        else:
            print('''You can't move the tile this direction
                  ''')
    except IndexError:
        print(''' You have pressed wrong key
              ''')


def turn_input():
    # enter your turn pattern
    turn = str(input_func(''' Enter your turn! (w s a d)
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
        print(''' You have pressed wrong key
        ''')


show_field()

# game cycle
while field != victory:
    turn_input()

print(' You are victorious! The number of your turns - ', count)

input_func()

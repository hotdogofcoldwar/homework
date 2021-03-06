﻿# -*- coding: utf-8 -*-

from __future__ import division

# homework #1 by Khalikov Murad

import sys

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input


# блок вопросов

ques1 = (u'Вопрос 1. Сколько будет (True+True)**(True+True+True)+True-False? ')
ques2 = (u'Вопрос 2. Сколько будет (True+True)**false? ')
ques3 = (u'Вопрос 3. Сколько будет int(str(a)*2)-int(int(a)*2)?, если a=2 ')
ques4 = (u'Вопрос 4. Переведите число 10110 из двоичной в десятичную систему ')
ques5 = (u'Вопрос 5. Какой символ появится после числа большего, чем int(sys.maxsize) в Python 2.7? ')
ques6 = (u'Вопрос 6. Введите результат действия 2*("10" in "1103") ')
ques7 = (u'Вопрос 7. Сколько будет len("100")+len("10")+len("1")? ')
ques8 = (u'Вопрос 8. int("1234567"[1:-2]) = ')

# блок ответов

ans1 = 9
ans2 = str('error')
ans3 = 18
ans4 = 22
ans5 = str('L')
ans6 = 2
ans7 = 6
ans8 = 2345


# текстовые строки

begin=(u'Здравствуйте! Ответьте, пожалуйста, на несколько вопросов. Если считаете, что результатом действия, описанного в вопросе, будет ошибка, укажите в качестве ответа error')

good=(u'Правильный ответ!')

result1=(u'Это был последний вопрос. Ваш результат: правильных ответов - ')
result2=(u' из ')
result3=(u'; количество попыток - ')
result4=(u', процент правильных ответов - ')


queslist = [ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8]
anslist = [ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8]

#count
right=0
wrong=0
i=0

print(begin)

for num in queslist:
    attempt=input_function(queslist[i])
    try:
        if str(attempt)==str(anslist[i]):
            print(good)
            right+=1
        else:
            if int(attempt)==int(anslist[i]):
                print(good)
                right+=1
            else:
                wrong+=1
                print(u'Неправильный ответ, попробуйте ещё раз')
                attempt=input_function(queslist[i])
                if attempt==anslist[i]:
                    print(good)
                    right+=1
                else:
                    if int(attempt)==anslist[i]:
                        print(good)
                        right+=1
                    else:
                        wrong+=1
                        print(u'К сожалению, нет. Правильный ответ - '), anslist[i]
    except ValueError:
        print(u'Кажется, вы ввели совсем не то, что нужно! Например, букву вместо числа. Попробуйте снова.')
        wrong+=1        
        attempt=input_function(queslist[i])
        try:
            if attempt==anslist[i]:
                print(good)
                right+=1
            else:
                if int(attempt)==anslist[i]:
                    print(good)
                    right+=1
                else:
                    wrong+=1
                    print(u'К сожалению, нет. Правильный ответ - '), anslist[i]
        except ValueError:
            print(u'Кажется, вы ввели совсем не то, что нужно! Например, букву вместо числа. Перейдем к другому вопросу. А правильный ответ - '), anslist[i]
            wrong+=1
    i+=1

print(u'Это был последний вопрос. Ваш результат - '),right,result2,i,result3,right+wrong,result4,int((right/(wrong+right))*100)

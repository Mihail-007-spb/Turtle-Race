"""Game-bet: The race of two turtles. Winning randomly."""

"""Игра-ставка: Забег двух черепашек. Выигрыш случайным образом."""


print()
print()
print('''Сейчас сыиграем в игру "Бег черепашек".
Играет два игрока, победит тот, чья черепашка
быстрее дойдет до финиша.''')
print()
name = input("И так, если готовы - нажмите ENTER: ")
print()


name1=input('''Введите имя "ПЕРВОГО игрока" нажмите ENTER: ''')
a=plauer1= str (name1)
print()
print(f"*******Привет, {name1}!*******")
print()

name2=input('''Введите имя "ВТОРОГО игрока" нажмите ENTER: ''')
b=plauer2= str (name2)
print()
print(f"*******Привет, {name2}!*******")
print()

import time
print('Проводим жеребьевку и.........................')
print()

import random
perv=random.randint(0, 1)
if perv==0:
    time.sleep(2)
    print ('ПЕРВАЯ сверху черепашка у хозяина %s.' % (a))
    print ('ВТОРАЯ сверху черепашка у хозяина %s.' % (b))
    print()
    print('******* ДЕЛАЙТЕ ВАШИ СТАВКИ НА ПОБЕДИТЕЛЯ ******')
    print()
    
if perv==1:
    time.sleep(2)
    print ('ПЕРВАЯ сверху черепашка у хозяина %s.' % (b))
    print ('ВТОРАЯ сверху черепашка у хозяина %s.' % (a))
    print()
    print('******* ДЕЛАЙТЕ ВАШИ СТАВКИ НА ПОБЕДИТЕЛЯ ******')
    print()
print('Жеребьевка= %s' % (perv))
print()

import turtle


t1 = turtle.Pen()
t1.pensize(5)
t1.color(1,0,0)
t1.up()
t1.back(300)
t1.down()

t2 = turtle.Pen()
t2.pensize(5)
t2.color(0,0,1)
t2.up()
t2.back(300)
t2.left(270)
t2.forward(50)
t2.left(90)
t2.down()


t= turtle.Pen()


t.color(0,0,0)
t.penup()
t.goto(-325,10)
t.write("Черепашка №1", align = "center"
        , font = ("Times", 10, "bold"))


t.color(0,0,0)
t.penup()
t.goto(-325,-80)
t.write("Черепашка №2", align = "center"
        , font = ("Times", 10, "bold"))






t.color(0,0,0)
t.penup()
t.goto(-300,50)
t.write("Старт", align = "center"
        , font = ("Times", 15, "bold"))


t.color(0,0,0)
t.penup()
t.goto(300,50)
t.write("Финиш", align = "center"
        , font = ("Times", 15, "bold"))


t7 = turtle.Pen()
t7.pensize(1)
t7.color(0,0,0)
t7.penup()
t7.goto(300,25)
t7.left(270)
t7.down()
t7.forward(100)
t7.up()
t7.forward(500)



t.color(1,0,0)
t.penup()
t.goto(0,250)
t.write("ЧЕРЕПАШКИ ВПЕРЕД!!!", align = "center"
        , font = ("Times", 25, "bold"))
t.up()
t.forward(1000)



z1=0
z2=0
s1=num1=0
s2=num2=0
time.sleep(5)

while True:
    num1=random.randint(10, 30)
    num2=random.randint(10, 30)
    
    try:

        if num1>=10 and num1<=30 and s1<600:
            s1=s1+num1
            z1=z1+1
            time.sleep(1)
            t1.forward(num1)
            print('Черепашка №1: %s' % (num1))

        if num1>=10 and num1<=30 and s1>=600 and z1-z2==0:
            break
            
        #Черепашка 2-ая сверху 
        if num2>=10 and num2<=30 and s2<600:
            s2=s2+num2
            z2=z2+1
            time.sleep(1)
            t2.forward(num2)
            print('Черепашка №2: %s' % (num2))
            print()
        
        if num2>=10 and num2<=30 and s2>=600:
            break

    except:
        
        if num1==0:
            print()
            
        if num2==0:
            print()

t.color(1,1,1)
t.penup()
t.goto(0,250)
t.write("ЧЕРЕПАШКИ ВПЕРЕД!!!", align = "center"
        , font = ("Times", 25, "bold"))


t.color(0,1,0)
t.penup()
t.goto(0,180)
t.write("Урааа ПОБЕДА!!!", align = "center"
        , font = ("Times", 35, "bold"))


t.color(1,0,0)
t.penup()
t.goto(0,20)
t.write('''Первая черепашка прошла: %s метров. ''' % (s1), align = "center"
        , font = ("Times", 15, "bold"))


t.color(0,0,1)
t.penup()
t.goto(0,-80)
t.write('''Вторая черепашка прошла: %s метров. ''' % (s2), align = "center"
        , font = ("Times", 15, "bold"))





print()
print('ПЕРВАЯ сверху черепашка прошла: %s метров.' % (s1))
print('ВТОРАЯ сверху черепашка прошла: %s метров.' % (s2))
print()


f1=abs(s1)
f2=abs(s2)

if f1>f2 and perv==0:
    print ('******* Победила черепашка хозяина: %s *******' % (a))

    t.color(0,1,0)
    t.penup()
    t.goto(0,-200)
    t.write('''Победила черепашка хозяина: %s ''' % (a), align = "center"
        , font = ("Times", 25, "bold"))

    

if f2>f1 and perv==1:
    print ('******* Победила черепашка хозяина: %s *******' % (a))

    t.color(0,1,0)
    t.penup()
    t.goto(0,-200)
    t.write('''Победила черепашка хозяина: %s ''' % (a), align = "center"
        , font = ("Times", 25, "bold"))


    


if f1<f2 and perv==0:
    print ('******* Победила черепашка хозяина: %s *******' % (b))
    
    t.color(0,1,0)
    t.penup()
    t.goto(0,-200)
    t.write('''Победила черепашка хозяина: %s ''' % (b), align = "center"
        , font = ("Times", 25, "bold"))

    

if f2<f1 and perv==1:
    print ('******* Победила черепашка хозяина: %s *******' % (b))

    t.color(0,1,0)
    t.penup()
    t.goto(0,-200)
    t.write('''Победила черепашка хозяина: %s ''' % (b), align = "center"
        , font = ("Times", 25, "bold"))



if f1==f2:
    print ('Удивительно, но......НИЧЬЯ')
    
    t.color(0,0,0)
    t.penup()
    t.goto(0,-200)
    t.write(''' Удивительно, но......НИЧЬЯ ''' % (b), align = "center"
        , font = ("Times", 25, "bold"))



        
        
    
    









    

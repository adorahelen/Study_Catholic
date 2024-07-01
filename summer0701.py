import turtle, random
front = 'img/front.gif'
back = 'img/back.gif'
dice1 = 'img/dice1.gif'
dice2 ='img/dice2.gif'
dice3 ='img/dice3.gif'
dice4 = 'img/dice4.gif'
dice5 ='img/dice5.gif'
dice6 ='img/dice6.gif'

scr = turtle.Screen()
scr.addshape(front)
scr.addshape(back)

t = turtle.Turtle()

coin = random.randint(0, 1)
if coin ==0: t.shape(front)
else : t.shape(back)

scr.exitonclick()

# src = turtle.Screen() || turtle.getscreen(), .addshape(이미지파일 문자열), t.stamp()

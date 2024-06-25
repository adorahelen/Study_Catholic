# print("시간순삭 파이썬")
# print("9*8은 72입니다.")
# print("9*8은", 9*8, "입니다.")
# print("반짝"*2, "눈이부셔", "No"*5)

import turtle as t
t.shape("turtle")
# t.shae (종류는, 에로우, 트라이앵글, 클래식)
# t.circle(100)
t.width(5)
t.color("red")
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
#각도에 따라, 각도를 몇으로 나누어서 고개를 돌리냐에 따라 달라짐

#리본 그리기, 

t.goto(60, 60)
t.goto(120,0)
t.goto(0,0)

t.color("blue")
t.goto(0,-70)
t.goto(120, -70)
t.goto(120, 0)
t.up()
t.goto(200, 50)
t.down()

t.color("green")
t.circle(50)
# t.goto(200, -80)

t.color("brown")
t.goto(190, 50)
t.goto(190, -80)
t.goto(200, -80)
t.goto(200, 50)

#집 모양을 그려라 + 나무도 그려라

window = t.Screen()
window.exitonclick()

#터틀 그래픽 정리1 
#import 를 통해 tuttle 라이브러리라를 가져온다. 
# t = turtle.Turtle() 혹은 import turtle as t로 객체 생성 t = turtle.Pen
# t.forward() 픽셀만큼 앞으로 이동  = t.fd
# t.backward(픽셀) : 만큼 뒤로 이동 t.back 가능 t.back, t.bk
# t.left() t.lt
# t.right()  머리 각도 조절 t.rt
# t.shape() 모양 arrow, circle, square, triangle, classcic 
# t.width() 굵기 t.pensize
# t.color() 색 #000000 ~ #ffffff *문자열로 지정해야함, 중요 2개씩 끊어서 R G B 16진수로 
# t.up() 붓을 올려서 움직여도 그어지지 않는 상태 t.penup(), t.pu()
# t.down() 붓을 내려서 그어지는 상태 t.pendown(), t.pd()
# t.goto() 좌표값을 지정해서 이동
# t.circle() 반지름을 통해 원을 생성 (음수면 반 시계 방향으로 그림)

#드디어 변수란 무엇인가

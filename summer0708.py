# # import turtle, random


# # # t = turtle.Turtle()

# # # dice1 = 'img/dice1.gif'
# # # dice2 ='img/dice2.gif'
# # # dice3 ='img/dice3.gif'
# # # dice4 = 'img/dice4.gif'
# # # dice5 ='img/dice5.gif'
# # # dice6 ='img/dice6.gif'
# # # scr = turtle.Screen()
# # # scr2 = turtle.Screen()
# # # scr.addshape(dice1)
# # # scr.addshape(dice2)
# # # scr.addshape(dice3)
# # # scr.addshape(dice4)
# # # scr.addshape(dice5)
# # # scr.addshape(dice6)
# # # lista = [dice1, dice2, dice3, dice4, dice5, dice6]

# # # while True:
# # #     a= random.choice(lista)
# # #     b= random.choice(lista)
# # #     if a == b :break
# # #     else : continue 

# # # window = turtle.Screen()
# # # window.exitonclick()

# # # import random, turtle
# # # scr = turtle.Screen()
# # # t = turtle.Turtle()
# # # dice = []
# # # for i in range(6):
# # #     dice.append(f"img/dice[i+1].gif")
# # #     scr.addshape(dice[i])
# # # cnt = 1

# # # while True:
# # #     f_dice = random.randint(1, 6)
# # #     s_dice = random.randint(1, 6)
# # #     t.up()
# # #     t.goto(-100, 0)
# # #     t.shape(dice[f_dice-1])
# # #     t.stamp()
# # #     t.goto(100, 0)
# # #     t.shape(dice[f_dice-1])
# # #     t.stamp()
# # #     if :
# # #     else:

# # # lista = [0] * 7
# # # lista2 = [0] * 7
# # # #리스트 선언시 곱하기 추가해주기

# # # i = 0
# # # for i in range(i, 7):

# # #     lista[i] = random.randint(50, 100)
# # #     lista2[i] = random.randint(50, 100)

# # # for i in range (7):
# # #     if lista[i]  >= 70 and lista2[i] >= 70:
# # #         print(i, end="")
# # #         #인덱스 쓰지 않고 위와 같이 써도 ㄱ핸찮
# # #         print(" 승진대상")
    

# # #함수 : 여러개 명령을 하나로 묶어놈
# # #클래스 : 함수와 변수들을 묶어듬
# # # 모듈 : 전부 묶어둠, 여러개의 함수들이 import random, turtle



# # # def lion(a):
    
# # #     if a < 0: print("양수") 
# # #     elif a == 0: print("영")
# # #     else : print("양수")

# # # a = int(input())
# # # lion(a)

# # # def lionking():
    
# # #     a = int(input())
# # #     if a < 0: print("양수") 
# # #     elif a == 0: print("영")
# # #     else : print("양수")
# # # lionking()

# # # def mulmul():
# # #     a = int(input())
# # #     b = int(input())
# # #     print(a*b)
# # # mulmul()


# # # a = int(input())
# # # b = int(input())
# # # def mulmul2(a,b):

# # #     print(a*b)
# # # mulmul2(a,b)

# # # def cal(rad):
# # #     area = 3.14 * rad **2
# # #     return area
# # # cc = cal(5.0)
# # # print(cc)

# # # asum = cal(5.0) + cal(10.0)
# # # print(asum)

# # # def udge(num):
# # #     if num%2 == 0:
# # #         print("짝수")
# # #         return 
# # #     print("홀수")
# # # num = int(input())
# # # udge(num)

# # # a = int(input())
# # # def one(a):
# # #     if a == 0: print(False)
# # #     else: print(True)

# # # def two(a):
# # #     return

# # # def three(a):
# # #     if a == 0: a = (False)
# # #     else: a= (True)
# # #     return a

# # # def four(a):
# # #     return 뭘 네가지 라는거지?

# # # 매개변수 있/없, 반환값 있/없
# # # def lalala():
# # #     a= 2
# # #     b = 0
# # #     if a == b : 
# # #         return 1
# # #     else : 
# # #         return 2
    
# # # def lalala2():
# # #     a= 2
# # #     b = 0
# # #     if a == b : 
# # #         return 1
    
# # #     return 2
# # t = turtle.Turtle()
# # length2 = random.randint(3, 6)

# # def squsqu(length):
# #     for i in range (length2):
# #         t.fd(length)
# #         t.lt(90)



# # def squsqu2(length):
# #     t.goto(-150, -150)
# #     for i in range (length2):
# #         t.fd(length)
# #         t.lt(90)
      



# # squsqu(100)
# # squsqu2(100)
# # window = t.screen()


# import turtle
# import random

# # Turtle 초기 설정
# screen = turtle.Screen()
# screen.title("랜덤 도형 그리기")
# screen.bgcolor("white")

# # Turtle 객체 생성
# drawer = turtle.Turtle()
# drawer.speed(0)  # 가장 빠른 속도로 그리기
# drawer.hideturtle()  # 터틀 숨기기

# # 도형 그리기 함수
# def draw_shape(turtle_obj, sides, length):
#     """주어진 sides와 length로 다각형을 그리는 함수"""
#     angle = 360 / sides
#     for _ in range(sides):
#         turtle_obj.forward(length)
#         turtle_obj.left(angle)

# # 도형의 색상 리스트
# colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"]

# # 랜덤 도형 그리기
# for _ in range(10):  # 10개의 도형을 그립니다
#     sides = random.randint(3, 10)  # 3에서 10 사이의 랜덤한 변의 수
#     length = random.randint(50, 150)  # 50에서 150 사이의 랜덤한 변의 길이

#     # 랜덤 색상과 위치 설정
#     drawer.color(random.choice(colors))
#     drawer.penup()
#     drawer.goto(random.randint(-300, 300), random.randint(-300, 300))  # 랜덤 위치로 이동
#     drawer.pendown()
    
#     # 도형 그리기
#     draw_shape(drawer, sides, length)

# # 종료 대기
# screen.mainloop()


import turtle
import random

# 초기 설정
screen = turtle.Screen()
screen.title("랜덤 도형 그리기")
screen.bgcolor("white")

# 거북이 생성
t = turtle.Turtle()
t.speed(0)  # 최대 속도

# 도형 그리기 함수
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.left(angle)

# 랜덤 위치로 이동
def move_to_random_position():
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()

# 랜덤 색상 설정
def set_random_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.color(random.choice(colors))

# 랜덤 도형 그리기
for _ in range(2):  # 도형의 개수를 2개로 제한
    sides = random.randint(3, 12)  # 3변부터 12변까지 무작위 선택
    set_random_color()
    move_to_random_position()
    draw_shape(sides)

# 프로그램 종료 대기
screen.mainloop()

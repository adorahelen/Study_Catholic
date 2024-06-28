# import turtle 
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("input your name", "input your ")
# t.up()
# t.goto(0, 250)
# t.write(s + "HIIIIi", False, "center", ("",24, "bold") )

# t.goto(-50, -50)
# t.down()

# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.seth(90)

# t.up()
# t.goto(0,0)

# window = turtle.Screen()
# window.exitonclick()

# s = input("평문 : ")
# print(s[-1::-1])

# two = s[1:len(s)-1:1]
# print(two)

# three = s[0]
# four = s[-1]
# # print(three + s[-2::-1]  + four) 내가 짠 코드, 밑에는 정답코드
# print(three+ s[-2:-len(s):-1] +four)

# import time 수정필요
# now = time.time()
# thisYear = int( 1970+now // 365*24*3600)
# print(f" Today is {thisYear} years ")
# s = input("so, what is your age? ")
# i = int(s)
# print(f"you are in 2050, {i+2050-thisYear}")

#조건문 시작
# 1. 순차구조 2. 선택구조 3. 반복구조

# score = int(input(" : "))
# if score >= 90:
#     print("A")
# else: print("F")

# i = int(input( " : " ))
# if i == 1 : print("Hello ")
# else : print("Norello")

# if i % 2 == 0: print("짝수 데스")
# else : print("홀수 데스 ")

# 3 > 4 and 10 <= 100 
# 1,0   and 1,0
# 앞이 0 이면 뒤는 보지도 않고 바로 False
# *논리회로를 떠올리면 된다.
# and는 곱하기 무조건 둘다 True(1)
# or은 더하기,
# 따라서 앞에 하나가 1나오면 뒤는 보지도 않고 True(1)
# : 단축평가
# if 3>7 and 10<100 and 200 > 3 도 앞에 하나 False면 뒤에는 볼 필요도 없다(단축평가)


# grade < 3.5 and year >= 2
# product == "참기름" and cnt != 0
# score >= 210 or obj == "Pass"
# score >= 60 and score <= 90
# 혹은 파이썬만 되는게 60 <= score <= 90 
# choice == 1 or 3 *이러면 안된다. True 혹은 False가 나와야 해서,  choice == 1 or choice == 3
# *바로 위는 무조건 참이 된다. 왜냐하면 0은 False 그 이외는 무조건 참이라서 1 or 3은 True or True

# score = int(input(" : "))
# if  100 >= score >= 90: print("A")
# elif 90> score >= 80: print("B")
# elif score >= 70: print("C")
# elif score >= 60: print("D")
# elif  0<= score <= 59 : print("F") 
# else: print("잘못 입력하셨습니다.")
# 110 입력하면 C 나옴, 따라서 범위 지정해야하고 -1은 쭉쭉 걸러지다 else 걸려서 잘못입력이라 나옴

# a,b,c = input(" : ").split(" ")
# a,b,c = int(a), int(b), int(c)
# if (a**2 + b**2 == c**2): print("직각삼각횽")
# else : print("노직각")

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.penup()
# t.goto(100, 100)
# t.write("입력된 정수는 양의 정수입니다.")
# t.goto(100, 0)
# t.write("입력된 정수는 0입니다.")
# t.goto(100, -100)
# t.write("입력된 정수는 음의 정수 입니다.")


# t.goto(0,0)
# t.pendown()
# n = int(turtle.textinput("", "숫자를 입력하세요."))

# if n > 0: t.goto(100, 100) 
# elif n == 0: t.goto(100, 0)
# else : t.goto(100, -100)

# window = turtle.Screen()
# window.exitonclick()

# import random
# c = random.randint(1, 100) #사이이 값 중 하나가 변수에 저장됨
# a = random.randrange(101, 1000, 2) #101부터 1000까지 2씩, 2씩이니까 짝수들 중 하나 반환
# b = random.randrange(10000) #stop 만 들어감, 그 전 값을 하나 반환

# print("주민등록번호의 성별 정보 번호를 생성한다. ")

# gen = random .randint(1,4)
# gen = random.randrange(1, 5)
# gen = random.randrange(1, 5, 1)
# gen = random.randrange(4) + 1
# print(f"created num is {gen}")

# if gen == 1 or gen == 3: print( "is ir man")
# else : print(" is it woman ")

import turtle, random

# t = turtle.Turtle()
# t.shape("turtle")

front = 'img/front.gif'
back = 'img/back.gif'
# dice1 = 'img/back.gif'
# dice2 ='img/back.gif'
# dice3 ='img/back.gif'
# dice4 = 'img/back.gif'
# dice5 ='img/back.gif'
# dice6 ='img/back.gif'

src = turtle.Screen()
# src2 = turtle.getscreen()


src.addshape(front)
src.addshape(back)
t = turtle.Turtle()

coin = random.randint(0, 1)
if coin ==0: t.shape(front)
else : t.shape(back)

# t.stamp()

# window = turtle.Screen()
src.exitonclick()


# window = turtle.Screen()
# window.exitonclick()
# src = turtle.Screen() || turtle.getscreen(), .addshape(이미지파일 문자열), t.stamp()


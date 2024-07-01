# import turtle, random
# front = 'img/front.gif'
# back = 'img/back.gif'
# dice1 = 'img/dice1.gif'
# dice2 ='img/dice2.gif'
# dice3 ='img/dice3.gif'
# dice4 = 'img/dice4.gif'
# dice5 ='img/dice5.gif'
# dice6 ='img/dice6.gif'

# scr = turtle.Screen()
# scr2 = turtle.Screen()
# scr.addshape(front)
# scr2.addshape(back)
# scr.addshape(dice1)
# scr.addshape(dice2)
# scr.addshape(dice3)
# scr.addshape(dice4)
# scr.addshape(dice5)
# scr.addshape(dice6)


# t = turtle.Turtle()
# k = turtle.Turtle()

# coin = random.randint(0, 1)
# if coin ==0: t.shape(front)
# else : t.shape(back)

# coin = random.randint(1, 2)

# t.up()
# k.up()
# t.goto(-100,0)
# k.goto(100,0)
# t.stamp()
# k.stamp()

# if coin ==1: 
#     t.shape(back)
#     k.shape(back)
#     k.shape("turtle")
#     k.goto(-100, 100)
#     k.write("성공")
# elif coin ==2: 
#     t.shape(front)
#     k.shape(front)
#     k.goto(-100, 100)
#     k.write("성공")
# elif coin ==3: 
#     t.shape(front)
#     k.shape(back)
#     k.goto(-100, 100)
#     k.write("실패")
# elif coin ==4: 
#     t.shape(back)
#     k.shape(front)
#     k.goto(-100, 100)
#     k.write("실패")
# else : print(-1)


# scr.exitonclick()

# # src = turtle.Screen() || turtle.getscreen(), .addshape(이미지파일 문자열), t.stamp()

# # 상대경로 쓰는 방법  ./ 현재 위치는 생략 가능
# # a/../d/e/back.gif   =? ./../d/e/back.gif
# # a/../b/c/fornt.gif => ./b/c/front.gif

# # t.hideturtle() 터틀 숨기기, t.showturtle() 터틀보이게 하기, t.home() 터틀을 0,0 위치로 이동 

#찌릿찌릿 전기회로 
# a,b = input("1번, 2번 전지 유무 입력 y/n : ").split(" ")

# if a.upper() == 'Y' and b.upper() == 'Y':
#     print("직렬 불 들어온다 마")
# elif a.lower() == 'y' or b.upper() == 'y':
#     print("병렬 불 들어온다 마")
# else : print("불 없다")

# year = int(input("연도 입력해봐 : "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("윤녕")
# else : print("노윤년")

# a, b, c = input("a b c 입력해 : ").split(" ")
# a, b, c = int(a), int(b), int(c)

# D = b*b - 4*a*c
# if D > 0: print("실근")
# elif D == 0: print("중근")
# else : print("허근")

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# disit = 0
# x1, y1, r1 = turtle.textinput("", "큰원 중심좌표와 반지름을 순서대로 입력받는다. : ").split(" ")
# x1, y1, r1 = int(x1), int(y1), int(r1)

# x2, y2, r2 = turtle.textinput("", "큰원 중심좌표와 반지름을 순서대로 입력받는다. : ").split(" ")
# x2, y2, r2 = int(x2), int(y2), int(r2)

# t.up()
# t.goto(x1, y1)
# yy1 = y1 - r1
# t.goto(x1, yy1)
# t.down()
# t.circle(r1)
# t.up()
# t.goto(x2, y2)
# yy2 = y2 - r2
# t.goto(x2, yy2)
# t.down()
# t.circle(r2)
# disit = (x1-x2)**2 + (y1-y2)**2 * 0.5
# t.up()
# t.goto(0, 250)

# if disit == 0: t.write("동심원")
# elif disit == r1 - r2: ("내접")
# elif r1 -r2 < disit : t.write("두 점에서 만난다")
# elif disit > r1+r2 : t.write("만나지 않고 외부에 있다 ")
# elif disit == r1+r2 : t.write("외접")
# s = turtle.textinput("", "사각형이라고 입력하시오")
# if s == "사각형":
#     a = turtle.textinput("", "가로 길이 입력")
#     b = turtle.textinput("", "세로 길이 입력")
#     a= int(a)
#     b= int(b)
#     if a == b: 
#         t.fd(a)
#         t.left(90)
#         t.fd(a)
#         t.left(90)
#         t.fd(a)
#         t.left(90)
#         t.fd(a)
#         t.left(90)
#         t.write("정사각형")
#     else : 
#         t.fd(a)
#         t.left(90)
#         t.fd(b)
#         t.left(90)
#         t.fd(a)
#         t.left(90)
#         t.fd(b)
#         t.left(90)
#         t.write("직사각형")
# else: print("-1")

# window = turtle.Screen()
# window.exitonclick()


# s = turtle.textinput("", "도형을 입력하시오")
# if s == "직사각형" :
#     w = int(turtle.textinput("가로길이 입력: "))
#     h = int(turtle.textinput("세로 길이 입력 : "))
#     t.fd(w)
#     t.left(90)
#     t.fd(h)
#     t.left(w)
#     t.left(90)
#     t.fd(h)
#     t.lt(90)

# if s == "정삼각형" :
#     w = int(turtle.textinput("한변의 길이 입력: "))
   
#     t.fd(w)
#     t.left(120)
#     t.fd(w)
#     t.left(120)
#     t.fd(w)
#     t.lt(90)

# elif s == "원" :
#     w = int(turtle.textinput("" "한변의 길이 입력: "))
#     t.circle(w)

# 반복문 시작
# import random
# def apple ():
#     lista = []
#     for i in range (20):
#         lista.append(random.randint(1, 20))
        
#     return lista
    
# a = apple()

# def babana(a):
#     for i in range (20):
#         print(f"    {a[i]}", end="")
#         if i == 9: print("\n")
#     print("\n")


# babana(a)

# def melon(a):
#     sum = 0
#     sum2 = 0
#     for i in range (20):
#         sum += a[i]

#     print(sum)
#     k = len(a)
#     print(sum/k)

# melon(a)

# def calcla ():
#     result = 3.15 ** 2
#     return result

# r = float(input(""))
# a = int(input(" : "))
# area = calcla()
# print(area)
# name = 1

# def greet(name, msg = "asads"):
#     print(name + msg) 가능

# greet("asdasddddddddddddddddd")


# def greet(msg = "asads", name): 불가능
#  주의***디폴트 매개변수 다음애 non 디폴트 매개변수가 올 수 없다.
#     print(name + msg)

# greet("asdasddddddddddddddddd")

# 디폴트 매개변수 (인수)
# -디폴트 매개변수는 매개변수에 기본값을 설정한 것 
# 호출할 때 디폴트 매개변수 위치에 해당 인수값 생략이 가능


# fun1 (y = 7, z= 2, x= 1) 가능
# fun2 (5, z= 10, y=20) 가능
# fun3 (y= 10, 4 , z = 1) 불가능 
# 위치 인수가 키워드 인수 뒤에 올 수 없음 섞어서 쓴다면

# 또 터틀이야 하
# import turtle, random
# t = turtle.Turtle()
# t.shape("turtle")
# # t.circle(100)
# # turtle.textinput("", "다음")
# # t.clear()
# # t.circle(-100)
# # turtle.textinput("", "다음")

# def seting ():
#     position = random.randint(-200, 200)
#     return position 

# def ookisa():
#     ooki = random.randint(-200, 200)
#     return ooki

# def mainn():
#     while True:
#         n = turtle.textinput("", "개수")
#         n = int(n)
#         if 10 < n < 20:
#             break
#         else: continue
#     return n

# n = mainn()
# seting2 = seting()
# ookisa2 = ookisa()
# lista = []
# for i in range (20):
#     lista.append(random.randrange(1, 21))

# poly = random.choice(lista)

# for i in range(n):
#     t.circle(ookisa2)
#     t.goto(seting2, poly)


# window = turtle.Screen()

# size = random.ranint(50 , 100)

# x = random.randint(-200, 200)
# y = random.randint(-200, 200)
# t.up()
# t.goto(x, y)
# t.down()

# import turtle
# import random

# # Initialize the turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)


# # Function to get a random position
# def seting():
#     position = random.randint(-200, 200)
#     return position

# # Function to get a random size
# def ookisa():
#     size = random.randint(50, 100)
#     return size

# # Function to get the number of polygons from the user
# def mainn():
#     while True:
#         n = turtle.textinput("", "개수")
#         n = int(n)
#         if 10 < n < 20:
#             break
#         else:
#             continue
#     return n

# # Function to draw a polygon with 'sides' number of sides and 'length' side length
# def draw_polygon(sides, length):
#     angle = 360 / sides
#     for _ in range(sides):
#         t.forward(length)
#         t.left(angle)

# # Main logic
# n = mainn()

# for _ in range(n):
#     # Get random position, size and number of sides for the polygon
#     x = seting()
#     y = seting()
#     size = ookisa()
#     sides = random.randint(3, 10)  # Random number of sides for the polygon (3 to 10)
    
#     # Move turtle to the random position
#     t.up()
#     t.goto(x, y)
#     t.down()
    
#     # Draw the polygon
#     draw_polygon(sides, size)

# # Keep the window open until it is closed by the user
# turtle.done()

# def getvalue():
#     w = float(input())
#     h = float(input())
#     return w,h

# w, h = getvalue()

# def bmifun(w,h):
#     result = w/ (h*h)
#     return result

# result = bmifun(w,h) 

# print(result)

# 67.5
# 1.7
# 23.356401384083046

# def exchange(m ,c ):
#     if c in c_list:
#         m_code = c_list,index(c)
#     else:
#         print(-1)
#         return
#     result = round(m/rate[m_code], 2)
#     print(m, result, unit_[m_code])

# c_list = []
# unit = []
# rate = []
# m = input
# c = input
# exchange()

# 환율 변환기

# 예제 데이터
# c_list = ["USD", "EUR", "JPY", "KRW"]
# unit_ = ["달러", "유로", "엔", "원"]
# rate = [1.0, 0.85, 110.0, 1130.0]

# def exchange(m, c):
#     if c in c_list:
#         m_code = c_list.index(c)
#     else:
#         print(-1)
#         return
#     result = round(m / rate[m_code], 2)
#     print(m, unit_[m_code], "->", result, unit_[0])  # Assume the target is always the first unit in the list (e.g., USD)

# 사용자 입력 받기
# m = float(input("금액을 입력하세요: "))
# c = input("통화 코드를 입력하세요 (USD, EUR, JPY, KRW): ").upper()

# # 환율 변환 함수 호출
# exchange(m, c)

# exchangelist = [['미국', '달러', 1182.5], ['중국', '위안', 169.22], ['유럽', '유로', 1286.74], ['일본', '엔', 1078.14] ]
# #2차원리스트로 변경 

# while True:
#     a, b = input(" : ").split(" ")
#     if a not in exchangelist:
#         continue
#     else: 
#         break

# def exchange(a,b):
#      m_code = exchangelist.index(b)
#      result = round(a / rate[index], 2)
#      print(a, unit_[m_code], "->", result, unit_[0])  # Assume the target is always the first unit in the list (e.g., USD)



# exchange(a,b)

# def n_polygon(n, length):
#     for i in range(n):
#         t.fd(length)
#         t.left(360/n)

# import turtle
# t = turtle.Turtle()

# for i in range(20):
#     t.lt(20)
#     n_polygon(6, 100)

# window = turtle.Screen()
# window.exitonclick()

# import turtle

# def square(length):
#     for _ in range(4):
#         t.fd(length)
#         t.lt(90)

# def drawit(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.color("green")
#     square(50)
#     t.end_fill()

# # 메인 코드
# t = turtle.Turtle()
# window = turtle.Screen()

# # 클릭 이벤트 설정
# window.onscreenclick(drawit)

# # 프로그램이 끝나지 않도록 유지
# window.mainloop()


import turtle

def draw(x,y):
    t.goto(x, y)

t= turtle.Turtle()
t.pensize(10)
t.speed(0)
window = turtle.Screen()
window.onscreenclick(draw)
window.mainloop()
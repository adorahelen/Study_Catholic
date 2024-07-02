# count = 1
# sum = 0

# while count <= 100:
#     sum += count
#     count +=1

# print(sum)


# password = ""
# while password != "pythonisfun":
#     password = input("암호를 입력하시오 : ")
# print("로그린 성공")

# s = input(" : ")
# i = 1 슬라이싱 사용하기 위해 0 이아닌 1
# j = len(s)

# while i <= j:
#     print(s[:i])
#     i+=1

# while i <= j:
#     print(s[:i])
#     i += 1

# for i in range (5):
#     for j in range(10):
#         print("*", end='')
#     print("")

# n = int(input(" : "))

# for i in range (n):
#     for j in range (n):
#         print("*", end="")
#     print("")
#     n -= 1

# for i in range (n):
#     for j in range (n):
      
#         print("*", end="")
#     n -= 1
#     print("")

# for i in range (1, n+1):
#     print("*"*i)

# for i in range (4):
#     for j in range (4):
#         print("(%s, %s)" %(i,j), end=" ")
#         if j == 1:
#             break
#     print("")

# for n in range (10):
#     if n % 2 == 0:
#         continue
#     print(n ,end=" ")


# while 1 < n:
#     n -= 1
#     if n % 2 == 0:
#         continue
#     print(n, end=" ")
    

# while 1 < n:
#     if n % 2 == 0:
#         n -= 1
#         continue
#     else: 
#         print(n, end=" ")
#         n -= 1

# import turtle, random
# t = turtle.Turtle()
# n = random.randrange(100, 251)
# n = random.randrange(50, 251)

# while True:
    
#     k = turtle.textinput("다각형 입력해라", "3 ~ 12 중 하나 입력")
#     k = int(k)
    
#     if 3<= k <= 12: 
#          break
    

# for i in range(k):
#         t.fd(n)
#         t.lt(360/k)
        
# k = turtle.textinput("", " :")
# k = int(k)
# while True:
#     k = turtle.textinput("", " :")
    # k = int(k) 이러면 반복문 돌리면서 새로 입력받은 값이 정수형이 아닌 문자형으로 
    #TypeError: '<=' not supported between instances of 'int' and 'str'
#     if 3 <= k <= 6:
#         break

# k = int(k)
# for i in range (k):
#     t.circle(n)
#     t.left(360/5)
# t.shape("turtle")
# for i in range (300):
#     leng = random.randint(1, 100)
#     t.fd(leng)
#     angle = random.randrange(-180, 181)
#     t.rt(angle)

# window = turtle.Screen()


# import random
# score = 100
# count = 0
# room = random.randrange(1, 4)

# while True:
#     num = int(input(" 방번호를 입력하시오 : "))
#     if not 3>= num >= 1:
#         print("Error")
#         continue
#     if num == room:
#         print("범인를 잡았습니다.")
#         break

#     else: 
#         print("그 방엔 범인 없어용")
#         score -= 10
#         print(score)
#         if score <= 0:
#             break
#         count += 1
#         if count == 2:
#             print("초기화")
#             room = random.randrange(1,4)
#             count = 0

# room = random.randint(1, 3)
# if num == room:
#     print("범위를 잡았습니다.")
     
# else: 
#     print("그 방엔 범인 없어용")
#     count += 1

# while True :
    # room = random.randint(1, 3)
    # n = int(input("방 번호 입력"))
    # if n == room:
    #     print(" 굿잡")
    #     score += 100
    #     break

    # elif n < 3:
    #     print("Error ")
    # else: 
    #     print("그 방엔 범인 없어용")
    #     score -= 10

# print("게임 끝")
# print(f"{score} 점수 스코어임")

#몬두리안 화가 거북이짱 개념정리
# t.color 색은 색상코드나 문자로 지정 , t.color((r,g,b))or t.color(r,g,b) : ㄱ,ㅎ,ㅠ, 는 0.0부터 1.0 사이의 실수값
# 1. t.pencolor 2.t.fillcolor (선색과 채우기 색 ) t.speed 속도 지정 가능 0 , 10 , 6 ,3, 1
# = random.random 하면 0.0 에서 1.0t사이의 값

# import turtle, random

# r = random.random()
# g = random.random()
# b = random.random()

# t = turtle.Turtle()

# t.pensize(3)
# for i in range(20):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     z = random.randint(0, 300)
#     t. penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color(r,g,b)
#     t.begin_fill()
#     for j in range (4):
#         t.fd(z)
#         t.rt(90)
#     t.end_fill()

# t.shape("turtle")
# window = turtle.Screen()
# window.exitonclick()



# import turtle, random

# r = random.random()
# g = random.random()
# b = random.random()
# t = turtle.Turtle()
# t.pensize(10)
# t.speed(0)

# poly = random.randint(3, 12)
# a = random.randint(10, 20)
# k = random.randint(10, 100)

# for i in range(a):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     z = random.randint(10, 300)
#     t. penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color(r,g,b)
#     t.begin_fill()

#     for j in range (poly):
#         t.fd(k)
#         t.rt(360/poly)
#     t.end_fill()

# t.shape("turtle")
# window = turtle.Screen()
# window.exitonclick()


# n = int(input())

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=" ")


#유클리드 호제법
# n1 = int(input())
# n2 = int(input())

# if n1 < n2:
#     n1, n2 = n2, n1

# while n2 > 0:
#     r = n1%n2
#     n1, n2 = n2, r
# if n1 != 1:
#     print("두수의 최대 공약수 : ", n1)
# else :
#     print("두수는 서로소이다. ")


import random
t = 1
answer = random.randint(1, 100)
print("1부터 100까지의 숫자를 하나 맞춰보아라")
guess = int(input(" 숫자 : "))
while guess != answer:
    
    t += 1
    if guess < answer:
        print(" 쫌 더 ")
    elif guess > answer:
        print(" 아래로 ")
    guess = int(input(" 숫자 : "))

    if t == 5:
        break

if guess == answer:
    print(" 맞추심, 시도횟수는" , t)
else : print(f"실패, 정답은 {answer}, 시도횟수는 {t}")
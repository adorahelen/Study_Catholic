#내가 원하는 원 그리기 
# import turtle as t
# radius = int(input("원의 반지를을 입력하시오: "))
# color = input("원의 색깔을 입력하시오: ")
# t.color(color)
# t.begin_fill()
# t.circle(radius)
# t.end_fill()
# window = t.Screen()
# window.exitonclick()
# 1. 한변의 길이 입력받고
# 2. 색상 입력받고
# 3. 길이값과 색을 이용해 삼각형 그리기 t.forwaord and head angle 

# 반지름 입력, 원 3개 그리는데 20씩 증가 시키면서, 각 원은 다른 색으로, 왼쪽에서 오른쪽으로 
# t.shape("turtle")
# radius = int(input("반지름 길이를 입력하시오: "))
# color2 = input("색상을 입력하시오: ")
# t.color(color2)
# t.begin_fill()
# t.circle(radius)
# t.end_fill()
# t.up()
# t.forward(120)

# t.downblu
# color2 = input("색상을 입력하시오: ")
# t.color(color2)
# t.begin_fill()
# t.circle(radius+20)
# t.end_fill()
# t.up()

# window = t.Screen()
# window.exitonclick()

# 측정시간 입력(초) , 자신의 위치에서 번개까지 거리 a*b
# see = int(input(" 측정한 시간을 입력하시오: "))
# a = 340 * see
# print(f"번개까지의 거리는 {a}") 
# print("번개까지의 거리는 %s" %a)
# print("번개까지의 거리는 {}".format(a))
# 쉼표랑, str 형변환 햇갈림 2개더 익숙해지기 

#문자열과 숫자를 하나씩 입력, 입력한 문자열이 입력한 숫자만큼 반복하여 출력되게한다.
# a = int(input("숫자 하나를 입력하시오 : "))
# b = input("문자열을 입력하시오 : ")
# print(b * a)

#3장 어디에나 있는 수식 
# 나누기 / 는 4/7에다가 1.75(소수점까지 나옴, 특이) = 실수 나눗셈
# 나누기(몫) 4/7하면 1나옴 (소수점 버림) = 정수 나눗셈
# 어떤수를 3 % 하면 무조건 0, 1, 2, 중에 하나가 나옴 
#또 어떤수를 7 % 하면 무조건 0 ~ 6 중에 하나가 나옴 

# n = int(input("초를 입력하시오 : "))
# min = n // 60
# sec = n % 60
# print(f"{min}분 {sec}초")

# x = 100
# y = 100

# x = y = 200
# print(x, y)

# x, y, z = input("수 세개 입력").split(" ")
# x, y, z = int(x), int(y), int(z)
# result = ((x+y+x)/3)
# print(f"{(x+y+z)/3:.2f}")
# print("%.2f" %(result))

# round 함수를 통한 소수점 제어 방식 (반올림 자동으로 진행되며 콤마를 통해 자리 지정)
# print("평균점수: ", round(3.141592, 2))
# print("평균점수: ", str(round(3.141592, 2)))
# print("평균점수: ", round(3.141592))

# print("평균점수: {:.2f}".format(123123.741592))
# print("평균점수: {:,.0f}".format(123123.741592))

# print("%7.2f" %(123.213122312332231))
# print("%5.2f" %(123.213122312332231))
# a.bf
# a는 자릿수를 확보하라는 명령인데, 기본 디폴트 자릿수(출력되는)보다 작으면 무시되고 더 크면 반영됨
# b는 알다싶이 소수점 이하의 자릿수 

# print(f"{30000.141592:30,.10f}")

# x = -1
# y = 3
# result = ((-y)^3) + (2*x^2*y) 
# print(result)

# F = int(input("화씨온도 : "))
# C = (F-32) * (5/9)
# print(f"온도는 다음과 같다. {C:.2f}")
# print(" 온도는 다음과 같다. %.2f" %(C))
# print(" 온도는 다음과 같다. {:.2f}".format(C))

# print("온도는 다음과 같다 ", C) 얘네
# print("온도는 다음과 같다 " + str(C)) 헷갈림

#두 지점을 입력받아 두 지점 사이의 거리를 계산하는 프로그램
# x1, x2 = input("x1 , x2 입력 : ").split(" ")
# y1, y2 = input("y1 , y2 입력 : ").split(" ")
# x1, x2 = int(x1), int(x2)
# y1, y2 = int(y1), int(y2)

# print(x1, x2)
# print(y1, y2)

# distane = ((x2-x1)**2 + (y2-y1)**2) *0.5

# print(distane)

# import turtle 
# t = turtle.Turtle()
# t.shape("turtle")
# t.goto(0,0)
# t.setheading(45)
# t.forward(141.4)
# t.up()
# t.goto(0,0)
# t.down()
# t.setheading(0)
# t.fd(100)
# t.seth(90)
# t.fd(100)

# t1 = turtle.Turtle()
# t1.shape("turtle")
# t1.goto(0,0)
# t1.setheading(45)
# t1.forward(141.4)
# t1.up()
# t1.goto(0,0)
# t.down()
# t1.setheading(0)
# t1.fd(100)
# t1.seth(90)
# t1.fd(100)

# window1 = t.screen()
# window2 = t1.screen()
# window1.exitonclick()
# window2.exitonclick()


# import time
# fseconds = time.time()
# totalsec = int(fseconds)
# totalmin = totalsec // 60
# minute = totalmin % 60
# totalhour = totalmin // 60 
# realhour = totalhour%24 +9

# print(realhour, minute)
#1970년 부터 현재까지의 초를 임폴트 한다. (실수값이라int로 전환시킴) 
#위에는 전체초, 밑에 전체 분을 구함
# 그 다음은 현재분, 전체시, 현재시 


# inputmon = int(input("돈 넣어라 : "))
# buywhat = int(input("니가 살 물건 가격 : "))

# result = inputmon - buywhat
# print(f"넣은 돈 {inputmon}, 사실 물건의 가격{buywhat}, 거스름돈{result}")
# coin500 = result // 500

# result = result % 500 
# coint100 = result // 100

# print(coin500)
# print(coint100)

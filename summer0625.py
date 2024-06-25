# print("시간순삭 파이썬")
# print("9*8은 72입니다.")
# print("9*8은", 9*8, "입니다.")
# print("반짝"*2, "눈이부셔", "No"*5)

# import turtle as t
# t.shape("turtle")
# t.shae (종류는, 에로우, 트라이앵글, 클래식)
# t.circle(100)
# t.width(5)
# t.color("red")
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

# t.goto(60, 60)
# t.goto(120,0)
# t.goto(0,0)

# t.color("blue")
# t.goto(0,-70)
# t.goto(120, -70)
# t.goto(120, 0)
# t.up()
# t.goto(200, 50)
# t.down()

# t.color("green")
# t.circle(50)
# # t.goto(200, -80)

# t.color("brown")
# t.goto(190, 50)
# t.goto(190, -80)
# t.goto(200, -80)
# t.goto(200, 50)

#집 모양을 그려라 + 나무도 그려라

# window = t.Screen()
# window.exitonclick()

#터틀 그래픽 정리1 
#import 를 통해 tuttle 라이브러리를 가져온다. 
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
#변수의 이름 짓기
# 변수의 대입하기
# x = y = 100 = z 불가능
# x, y, z = 100 불가능

# x, y, z = 100, 200, 300 
# x = y = z = 100 
# x, y, z = 100, 100, 100
# x = 100, y = 100 불가능 , 때문에
# x = 100, 200 가능 튜플 자료형 

# x,y = 100, 200
# sum1 = x+y
# print("{} 그리고 {} 더한 값은 {} 입니다. " .format(x,y,sum1))
# print("%s 과 %s 합은 %s 입니다." %(x,y,sum1))
# print(str(x) + "와" + str(y) + "의 합은" + str(sum1) + "입니다.")
# print(f"{x}과 {y}의 합은 {sum1}입니다.")

# 1. 포멧함수 사용 2. 형식지정자 사용 3. 형변환 캐스팅과 + 연신자 사용 4. f string 함수 사용

#문자열 입력받기
# a = input("  이름을 입력하세요 : ")
# print(a, "씨 안녕하세요.")
# print("파이썬에 오신 것을 환영합니다.")

# num1 = input("기본적으로 모두 문자열로 입력받음")
# num1 = int(num1)
# num2 = int(input("수 입력해봐"))
# print(num1 + num2)
# num3 = input("실수 넣어조")
# num3 = float(num3)
# print(num3+num2)

# 스트링(기본 input 함수가) 아닌, 인트형으로 입력받을때는 문자나 실수가 입력되면 에러남 
# num1 = input("기본적으로 모두 문자열로 입력받음")
# num2 = input("수 입력해봐")
# print(num1 + num2)

# x = int(input("정수1 입력"))
# y = int(input("정수2 입력"))
# print(x, "+",  y, "=", x+y)

# print("{}에서 {}를 뺸 결과는 {}입니다." .f(x, y, x-y))
# 다음 문제를 포멧 형식으로 작성해보시오
#  => format 형식, %형식지정자 방식, f-string 방식 전부 숙지할 것

# 출력형태 정리!
# -, 콤마를 이용함
# - 출력할 변수 또는 문자열들을 콤마로 나열
# - 콤마 대신 공백이 출력됨

# - format 함수 이용시
# => { }중괄호를 출력할 값 변수나 문자열에 맞게 나열해서 사용
# => { }중괄호는 문자열 "   "안에 있어야함
# => 출력할값들은 .f .format() 안에 콤마로 나열
# :중괄호 안에 인덱스 사용 가능. 인덱스는 .format 안에 나열한 출력값 순서이며 가장 왼쪽이 0부터 시작

# - %형식 지정자 이용시
# => 변수 유형에 따라 %와 서식문자를 이용하여 출력형태를 지정
# => %s: 문자열 d는 정수 f는 실수
# => %s는 만능
# => 형식지정자와 출력할 값의 수가 동일해야한다.
# => 문자열 다음에 %와 괄호를 사용하ㅏ고 괄호 안에 출력 값을 나열 , 만약 값이 하나씩이면 괄호 생략

# - + 연결 연산자 이용시
# 숫자는 str () 형변환 으로 문자열 전환 후 연결

# f스트링 이용시 
# 출력할 문자열 앞에 f를 붙여줌
# => {}중괄호 안에 출력할 변수를 붙여줌 

# print("{} 그리고 {} 더한 값은 {} 입니다. " .format(x,y,sum1))
# print("%s 과 %s 합은 %s 입니다." %(x,y,sum1))
# print(str(x) + "와" + str(y) + "의 합은" + str(sum1) + "입니다.")
# print(f"{x}과 {y}의 합은 {sum1}입니다.")

# year = 1
# name = 'KIM'
# major = 'Computer'
# grade = 4.3
# avg = 3.7
# print("학년:", year, "이름:", name)
# print("학년:{} 이름:{} ".format(year, name))
# print("학년:{0} 이름{1}".format(year, name))
# print("level {0} name{1} what{1}".format(year, name))
# print(f"you level {grade}, name{name}")

# a = 10
# b = 30
# c = int(input())
# d = a+b+c

# #5가지 출력형태 전부 출력 *****
# print(f"{a} + {b} + {c} = {d}")

#내가 원하는 원 그리기 전까지 

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))

# print(f"{a} + {b} + {c} = {a+b+c}")
# print(f"{a} - {b} - {c} = {a-b-c}")
# print(f"{a} * {b} * {c} = {a*b*c}")
# print(f"{a} + {b} + {c} = {a+b+c}")

# print("%d + %d + %d = %d" %(a, b, c, a+b+c))
# print("%d - %d - %d = %d" %(a, b, c, a-b-c))
# print("%d * %d * %d = %d" %(a, b, c, a*b*c))
# print("%s / %s = %s" %(a, b, a/b))
# print("%d // %d = %d" %(a, b, a//b))
# print("%d %% %d = %d"%(a, b, a%b))
# print("%d ^ %d = %d"%(a, b, a**b))
# print("%s" %(min(a,b,c)))
# print("%s" %(max(a,b,c)))

# print("%d"%(a) ,end="") 줄바꿈 안하도록

# mon = int(input())

# mon_10000 = mon // 10000
# mon_1000 = (mon % 10000) // 1000
# mon_100 = (mon % 1000) // 100
# mon_10 = (mon % 100) // 10

# print(f"만원짜리 : {mon_10000} 개")
# print(f"천원짜리 : {mon_1000} 개")
# print(f"백원짜리 : {mon_100} 개")
# print(f"십원짜리 : {mon_10} 개")

#원기둥의 부피를 계산하는 프로그램 
# V = 3.141592
# Radius = float(input("원의 반지름을 입력하시오 : "))
# High = float(input("원의 높이를 입력하시오 : "))
# result = V * (Radius**2) * High

# print("%.2f"%(result))
# print(f"{result:.2f}")
# print("{:.2f}".format(result))
# print("어려워"+str(round(result, 2)))
# print("아", result)
# print("아아", round(result, 2))

# print(1+2j-3j)
# print("나는 현재 " + str(18) + " 입니다..")
# poem = f"""나는요
# 오빠가
# 좋은걸 '어"떻게 %d {12}
# 아베말 드리이이이이이임 """%(18)
# print(poem)

# s = "Hello Python"
# for i in range(0, 11):
#     print(s[i])

# i = 0
# while s != 0:
#     print(s[i])
#     i += 1
#     if i == 11:
#         break
# print(s[0:10])
# print(s[0:10:2])


# s = "Next time i fall in love"
# s = 'n' + s[1:]
# print(s[:])
# print(s[-1::-1])
# print(s[:9])
# print(s[5:])
# print(s[8:4:-1])
# print(s[-9:-13:-1])
# print(s[0:11])
# print(s[10:23])
# print(s[0:4:2])
# print(s[10:23:3])

# print(s[4:0])
# print(s[4:0:-1])
#문자열 거꾸로 출력하는 방법은 슬라이싱을 사용하는데 음수로 스텝을 지정
#문자열은 상수이기에 부분 변경이 불가능하다. 
#변경을 위해서는 슬라이싱을 추출하고 연결해주는 작업이 요구된다. 


 #소금물의 농도는
# salt = int(input(" 소금의 양 g : "))
# water = int(input(" 물의 양 : "))
# R = (salt /  (salt + water)) * 100
# print(f"소금물의 농도는 : {R:.2f}")

# print("안녕하세요!")
# name = input("당신의 이름은 무엇인가요? ")
# length = len(name)
# print(f"당신의 이름은 {length}글자네요 ")
# age = int(input("당신의 나이는 어떻게 되나요?"))
# print("내년이면" + str(age+1) + "살이 되네요")

# import turtle 
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("거북이거북이", "이름을 입력하세요 : ")
# t.write("안녕하세요" + s + "씨 만나서 반갑습니다. ")
# # t.write("adadada", True, )
# # ""창제목은 유지해야한다. 

# t.goto(0,300)
# t.write(s, False, "center", ("", 24, "bold"))
# t.down()


# t.goto(0,250)
# t.write(s, True, "left", ("", 24, "normal"))

# t.up()
# t.goto(0,200)
# t.write(s, True, "right", ("", 24, "italic"))
# t.up()
# t.goto(0,100)
# t.write(s, True, "center", ("", 24, "bold"))

# window = turtle.Screen()
# window.exitonclick()

# import turtle 
# t = turtle.Turtle()
# t.shape("turtle")
# s = int(turtle.textinput("반지름 입력받기", "반지름을 입력하시오 : "))
# t.up()
# t.goto(0, -s)
# t.down()
# t.circle(int(s))
# t.up()
# t.goto(0, 250)
# t.write("반지름" +str(s)+ "인 원", False, "center", ("", 24, "bold"))

# window = turtle.Screen()
# window.exitonclick()

import turtle
t = turtle.Turtle()
t.shape("turtle")

a,b,c,d = turtle.textinput("좌표입력","x1, y1, x2, y2 입력하시오").split(" ")
#처음에 입력을 받을때 한쌍이 (x1, y1) 그리고 (x2, y2) : -100 -100 100 100 이어야 하는데
#공식을 몰라서 -100 100 -100 100 이렇게 잘 못 들어가고 있었음 ;;;;;;;;;;;;;;;;;;
x1 = int(a)
y1 = int(b)
x2 = int(c)
y2 = int(d)
t.up()
t.goto(x1, y1)
t.down()
t.goto(x2,y2)
result = 0
result = (((x2- x1)**2) + ((y2-y1)**2)) **0.5
t.up()
t.goto(0, 250)
t.write("두점사이의 거리는" +str(result), False, "center", ("", 24, "bold"))
# t.write("두점사이의 거리는 %f"%(result), False, "center", ("", 24, "bold"))

window = turtle.Screen()
window.exitonclick()
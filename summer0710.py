# # # # # # import turtle
# # # # # # t= turtle.Turtle()
# # # # # # s= turtle.Screen()

# # # # # # s.onscreenclick(함수명):
# # # # # # 마우스 왼쪽 버튼을 클릭했을 때 실행 할 콜백함수 등록, s.onclick( 함수명, 1 or 2 or 3)
# # # # # # 1은 왼쪽, 2는 가운데, 3은 오른쪽 마우스 버튼을 의미한다. 

# # # # # #  s.onkey(함수명, "키이름"): 해당 키를 눌렀을 때 실행할 콜백함수를 등록, 키 이름은 생략 불가
# # # # # # s.onkeypress(함수명, "키이름")

# # # # # # s.listen()
# # # # # # s.mainloop

# # # # # # 키보드 ㅣ을 누르면 선분의 길이를 입력받는다 (초긱밧은 10, 10~`100`)사이로 제한 잘못 입력시 다시 입력
# # # # # # 키보드 s를 누르면 펜의 굵기를 입력받는다. ( 1~10 사이로 제한, 잘못 입력시 다시)
# # # # # # 키보드 a를 누르면 각도를 입력받는다. ( 0 ~ 360 사이로 제한, 잘못 입력시 다시 입력)
# # # # # # 방향키를 이용하여 선을 그린다. (up, Down : 앞으로, 뒤로)
# # # # # # 마우스를 이용하여 선의 위치를 변경할 수 있다.

# # # # # import turtle

# # # # # t = turtle.Turtle()
# # # # # s = turtle.Screen()

# # # # # # Initial values
# # # # # line_length = 10
# # # # # pen_width = 1
# # # # # angle = 0

# # # # # def set_line_length():
# # # # #     global line_length
# # # # #     length = s.textinput("Line Length", "Enter line length (10-100):")
# # # # #     if length:
# # # # #         try:
# # # # #             length = int(length)
# # # # #             if 10 <= length <= 100:
# # # # #                 line_length = length
# # # # #             else:
# # # # #                 s.textinput("Error", "Please enter a value between 10 and 100.")
# # # # #                 set_line_length()
# # # # #         except ValueError:
# # # # #             s.textinput("Error", "Invalid input. Please enter a number.")
# # # # #             set_line_length()

# # # # # def set_pen_width():
# # # # #     global pen_width
# # # # #     width = s.textinput("Pen Width", "Enter pen width (1-10):")
# # # # #     if width:
# # # # #         try:
# # # # #             width = int(width)
# # # # #             if 1 <= width <= 10:
# # # # #                 pen_width = width
# # # # #                 t.pensize(pen_width)
# # # # #             else:
# # # # #                 s.textinput("Error", "Please enter a value between 1 and 10.")
# # # # #                 set_pen_width()
# # # # #         except ValueError:
# # # # #             s.textinput("Error", "Invalid input. Please enter a number.")
# # # # #             set_pen_width()

# # # # # def set_angle():
# # # # #     global angle
# # # # #     angle_input = s.textinput("Angle", "Enter angle (0-360):")
# # # # #     if angle_input:
# # # # #         try:
# # # # #             angle_input = int(angle_input)
# # # # #             if 0 <= angle_input <= 360:
# # # # #                 angle = angle_input
# # # # #             else:
# # # # #                 s.textinput("Error", "Please enter a value between 0 and 360.")
# # # # #                 set_angle()
# # # # #         except ValueError:
# # # # #             s.textinput("Error", "Invalid input. Please enter a number.")
# # # # #             set_angle()

# # # # # def move_up():
# # # # #     t.setheading(90 + angle)
# # # # #     t.forward(line_length)

# # # # # def move_down():
# # # # #     t.setheading(270 + angle)
# # # # #     t.forward(line_length)

# # # # # def move_left():
# # # # #     t.setheading(180 + angle)
# # # # #     t.forward(line_length)

# # # # # def move_right():
# # # # #     t.setheading(0 + angle)
# # # # #     t.forward(line_length)

# # # # # def change_position(x, y):
# # # # #     t.penup()
# # # # #     t.goto(x, y)
# # # # #     t.pendown()

# # # # # # Key bindings
# # # # # s.onkey(set_line_length, "l")
# # # # # s.onkey(set_pen_width, "s")
# # # # # s.onkey(set_angle, "a")
# # # # # s.onkey(move_up, "Up")
# # # # # s.onkey(move_down, "Down")
# # # # # s.onkey(move_left, "Left")
# # # # # s.onkey(move_right, "Right")

# # # # # # Mouse binding
# # # # # s.onscreenclick(change_position)

# # # # # # Listen for events
# # # # # s.listen()
# # # # # s.mainloop()




# # # # # s = turtle.textinput("", "")

# # # # # import turtle
# # # # # t = turtle.Turtle()
# # # # # screen = turtle.Screen()
# # # # # t.shape("turtle")
# # # # # t.speed(0)

# # # # # def draw_maze(x, y):
# # # # #     for i in range (2):
# # # # #         t.penup()
# # # # #         if i == 1:
# # # # #             t.goto(x+100, y+100)
# # # # #         else:
# # # # #             t.goto(x, y)
# # # # #         t.pendown()
# # # # #         t.fd(300)
# # # # #         t.rt(90)
# # # # #         t.fd(300)
# # # # #         t.lt(90)
# # # # #         t.fd(300)

# # # # # def turn_left():
# # # # #     t.l,t(10)
# # # # #     t.fd(10)

# # # # # import turtle
# # # # # t= turtle.Turtle()
# # # # # t.shape("turtle")

# # # # # def input_line():
# # # # #     global length
# # # # #     # 지역변수 를 전역변수 만들기 자바의 퍼블릭도 동일한 기능?
# # # # #     msg = ""
# # # # #     while True:
# # # # #         length = int(turtle.textinput("",msg+" " ))
# # # # #         if 
# # # # #     s.listten()
# # # # # def input_ps():
# # # # #      msg = ""
# # # # #     while True:
# # # # #         length = int(turtle.textinput("",msg+" " ))
# # # # #         if 
# # # # #     s.listen()

# # # # # def input_angle():
# # # # #      msg = ""
# # # # #     while True:
# # # # #         length = int(turtle.textinput("",msg+" " ))
# # # # #         if 


# # # # # def forward_turtle():
# # # # #     t.forward(length)

# # # # # def backward_turtle():
# # # # #     t.backward(length)

# # # # # s = turtle.Screen()
# # # # # length = 10
# # # # # s.onkey(input_line, "l")
# # # # # s.onkey(input_ps, "s")
# # # # # s.onkey(input_angle, "a")
# # # # # s.onkey(forward_turtle, "Up")
# # # # # s.onkey(backward_turtle, "Down")
# # # # # s.onscreenclick(pos_move)
# # # # # s.listen()

# # # # import turtle

# # # # t = turtle.Turtle()
# # # # t.shape("turtle")

# # # # # Initial values
# # # # length = 10
# # # # pen_width = 1
# # # # angle = 0

# # # # def input_line():
# # # #     global length
# # # #     while True:
# # # #         try:
# # # #             user_input = turtle.textinput("Line Length", "Enter line length (10-100):")
# # # #             if user_input is None:
# # # #                 return  # User cancelled the input dialog
# # # #             length = int(user_input)
# # # #             if 10 <= length <= 100:
# # # #                 break
# # # #             else:
# # # #                 turtle.textinput("Error", "Please enter a number between 10 and 100.")
# # # #         except ValueError:
# # # #             turtle.textinput("Error", "Invalid input. Please enter a valid number.")
# # # #             s.listten()
    
# # # # def input_ps():
# # # #     global pen_width
# # # #     while True:
# # # #         try:
# # # #             user_input = turtle.textinput("Pen Width", "Enter pen width (1-10):")
# # # #             if user_input is None:
# # # #                 return  # User cancelled the input dialog
# # # #             pen_width = int(user_input)
# # # #             if 1 <= pen_width <= 10:
# # # #                 t.pensize(pen_width)
# # # #                 break
# # # #             else:
# # # #                 turtle.textinput("Error", "Please enter a number between 1 and 10.")
# # # #         except ValueError:
# # # #             turtle.textinput("Error", "Invalid input. Please enter a valid number.")
    
# # # # def input_angle():
# # # #     global angle
# # # #     while True:
# # # #         try:
# # # #             user_input = turtle.textinput("Angle", "Enter angle (0-360):")
# # # #             if user_input is None:
# # # #                 return  # User cancelled the input dialog
# # # #             angle = int(user_input)
# # # #             if 0 <= angle <= 360:
# # # #                 break
# # # #             else:
# # # #                 turtle.textinput("Error", "Please enter a number between 0 and 360.")
# # # #         except ValueError:
# # # #             turtle.textinput("Error", "Invalid input. Please enter a valid number.")

# # # # def forward_turtle():
# # # #     t.setheading(angle)
# # # #     t.forward(length)

# # # # def backward_turtle():
# # # #     t.setheading(angle + 180)  # Move in the opposite direction
# # # #     t.forward(length)

# # # # def pos_move(x, y):
# # # #     t.penup()
# # # #     t.goto(x, y)
# # # #     t.pendown()

# # # # s = turtle.Screen()
# # # # s.title("Turtle Control")

# # # # # Set initial pen width
# # # # t.pensize(pen_width)

# # # # # Key bindings
# # # # s.onkey(input_line, "l")
# # # # s.onkey(input_ps, "s")
# # # # s.onkey(input_angle, "a")
# # # # s.onkey(forward_turtle, "Up")
# # # # s.onkey(backward_turtle, "Down")

# # # # # Mouse binding
# # # # s.onscreenclick(pos_move)

# # # # # Start listening for events
# # # # s.listen()
# # # # s.mainloop()


# # # import turtle

# # # def f(x):
# # #     return x**2 + 1

# # # # Setup turtle
# # # t = turtle.Turtle()
# # # t.shape("turtle")
# # # t.speed(0)  # Set turtle speed to maximum

# # # # Setup screen
# # # s = turtle.Screen()
# # # s.setworldcoordinates(0, 0, 150, 22500)  # Set the world coordinates to fit the parabola

# # # # Draw the parabola
# # # for x in range(150):
# # #     t.goto(x, int(0.01 * f(x)))

# # # turtle.done()

# # # 신나는 재귀호출 

# # # def fact(n):
# # #     if n ==1:
# # #         return 1
# # #     else :
# # #         return n*fact(n-1)

# # # n = int(input(" 정수를 입력 : "))
# # # f = fact(n)
# # # print(f"{n}!은 {f}이다.")


# # # def rec_num (t):
# # #     if t >0: #끝나는 조건 
# # #         # print(t)
# # #         rec_num(t-1) #재귀재귀
# # #         print(t)
    

# # # rec_num(10)


# # # 신나는 딕셔너리 
# # # 딕셔너리는 중괄호를 이용하고, 쉼표로 나열 
# # # *여러개의 데이터를 한꺼번에 저장하고 처리한다
# # # 키 와 벨류의 짝을 이룸
# # # 키 값을 이용하여 자료에 접근 

# # bookbook = {"asdadasd" : "asdasads", "dsasd" : 111111, "dasddsa" : 2422124121}
# # print(bookbook)
# # print(bookbook["dsasd"]) #인덱스 사용은 불가합니다, 오직 키 (앞) 값으로만 접근합니다.

# # bookbook2 = {}
# # bookbook2["나나나"] = "01010101013"
# # bookbook2["나나나"] = "01010101012"
# # print(bookbook2)

# # p_book = {}
# # P_book2 = dict()

# # p_book["홍길동"] = '0101456879'

# # #리스트는 키로 사용할 수 없다. 

# # print(bookbook.keys())
# # for key in sorted(bookbook.keys()):
# #     print(key, bookbook[key])

# # print(bookbook.values())
# # print(bookbook.items())

# # # del(), pop() 함수로 삭제 가능 
# # del bookbook["asdadasd"]
# # print(bookbook)
# # bookbook = {"asdadasd" : "asdasads", "dsasd" : 111111, "dasddsa" : 2422124121}
# # print(bookbook)
# # a= bookbook.pop("asdadasd")
# # print(a)
# # print(bookbook)
# # print(a)
# # bookbook.clear()
# # print(bookbook)

# # book = {"asdsa" : "asdas", "asdasd" : "sasdsad", "asddsa" : "sadassa"}
# # if "asdsa" in book.keys(): #or book
# #     print(book["asdsa"])

# # print(book.get("asdsa"))
# # print(book.get("sdadasafasfafaasfafaas"))
# # print(book.get("asdsa2", "key no"))
# # print(book.get("asdsa2"))

# # del book['asdasd']
# # print(book)
# # if "asdsa" in book:
# #     del 

# items = {'커피' : 7, "펜" : 3, "종이컵" : 10, "우유" : 5, "콜라" : 4, "라면" : 11}
# for k in items:
#     print(k, end=" ")
# print()

# for k in items.keys():
#     print(k, end=" ")
# print()
# for k in items.values():
#     print(k, end=" ")
# print()
# for k in items.items():
#     print(k, end=" ")
# print()
# for k, v in items.items():
#     print(k,",", v)

# items = {'커피' : 7, "펜" : 3, "종이컵" : 10, "우유" : 5, "콜라" : 4, "라면" : 11}
# items_keys = items.keys()
# items_klist = list(items.keys()) # 리스트로 변환
# print(items_klist) 
# items_klist.append('사이다')
# print(items_klist)

# items_vlist = list(items.values()) # 리스트로 변환
# print(items_vlist[0]) 
# items_vlist.append(4)
# print(items_vlist)
#리스트 요소가 튜플 자료형임
#리스트로 변환했으니 리스트 함수 사용이 가능해졌다. 

list1 = [1,2,3,4,5]
tu1 = (1,2,3,4,5,)
dic1 = {1,2,4,5,6,}
s1 = set()
s2 = {1,2,5,2,2,2,22,2,2,22,2,22,2,22,2,2,2,2,2}
s2.add(2)
s1.add(6)
s1.add(7)
s1.add(22)

print(list1, type(list1))
print(tu1, type(tu1))
print(dic1, type(dic1))
print(s1, type(s1))
print(s2, type(s2))
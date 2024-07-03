# for i in range (5):
   
#     print("aaaaa", end=" ")
#     #range (start, stop, step)

# for i in range (1, 6, 1):
#     print(i, end=" ")

# sum = 0
# for i in range (1, 101, 1):
#     sum += i
#     print(sum)

# fac = 1
# n = int(input(" : "))
# for a in range(1, n+1):
#     fac = fac * a
# print(" 입력값의 팩토리얼은 ", fac)

# response = True
# while response != "그래":
#     response = input(" : ")
# print("탈출") 


# """
# 책에 나와있고, 사람이 작성한 거북이를 이용해 몬드리안 그림 그리기1 
# """
# import turtle, random

# t = turtle.Turtle()
# t.pensize(3)


# colors = ["red", "blue", "yellow"]

# for i in range (20):
#     # r = rgb(255, 0, 0)
#     # g = rgb(128, 0, 0)
#     # b = rgb(255, 255, 0)
#     color = random.choice(colors)

#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(1, 300)

#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()

#     for j in range (4):
#         t.forward(length)
#         t.right(90)

#     t.end_fill()

# window = turtle.Screen()
# window.mainloop()


# """
# 책에 나와있고, 사람이 작성한 거북이를 이용해 몬드리안 그림 그리기를 바탕으로
# 생성형 AI 에게 코드 보충을 시킨 거북이_몬드리안 그림 코드 1
# """
# import turtle
# import random

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(10)
# t.pensize(3)

# # Define colors and the dimensions of the rectangles
# colors = ["red", "blue", "yellow", "black", "white"]
# rectangles = [
#     {"color": "red", "x": -150, "y": 150, "width": 100, "height": 200},
#     {"color": "blue", "x": 0, "y": 150, "width": 200, "height": 100},
#     {"color": "yellow", "x": 150, "y": 50, "width": 100, "height": 100},
#     {"color": "black", "x": -150, "y": 0, "width": 200, "height": 100},
#     {"color": "white", "x": 50, "y": 0, "width": 100, "height": 100},
#     {"color": "yellow", "x": -150, "y": -150, "width": 100, "height": 100},
#     {"color": "blue", "x": -50, "y": -150, "width": 200, "height": 50},
#     {"color": "black", "x": 150, "y": -150, "width": 50, "height": 100},
#     {"color": "red", "x": 200, "y": -100, "width": 50, "height": 100},
#     {"color": "white", "x": -150, "y": -200, "width": 150, "height": 50},
# ]

# # Draw rectangles based on the defined dimensions and colors
# for rect in rectangles:
#     t.penup()
#     t.goto(rect["x"], rect["y"])
#     t.pendown()
#     t.color(rect["color"])
#     t.begin_fill()

#     for _ in range(2):
#         t.forward(rect["width"])
#         t.right(90)
#         t.forward(rect["height"])
#         t.right(90)

#     t.end_fill()

# # Set up the window and display the result
# window = turtle.Screen()
# window.mainloop()



# """
# 거북이를 이용해 몬드리안 그림 그리기2
# 실제 몬드리안 그림과 가장 근접하다!
# """

import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(10)
t.pensize(3)

# Define colors
colors = ["red", "blue", "yellow", "black", "white"]

# Define the grid size
grid_size = 50

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()

# Draw a random Mondrian-inspired pattern
for _ in range(20):  # Adjust the number of rectangles
    color = random.choice(colors)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    width = random.randint(1, 6) * grid_size
    height = random.randint(1, 6) * grid_size
    draw_rectangle(x, y, width, height, color)

# Set up the window and display the result
window = turtle.Screen()
window.mainloop()

#정해진 격자 범위를 벗어나지 않으면서, 몬드리안 그림의 사용된 5가지 색상만을 기준으로 그림을 그린다. (랜덤으로 사각형을)
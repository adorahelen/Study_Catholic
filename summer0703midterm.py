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

import turtle, random

t = turtle.Turtle()
t.pensize(3)


colors = ["red", "blue", "yellow"]

for i in range (20):
    # r = rgb(255, 0, 0)
    # g = rgb(128, 0, 0)
    # b = rgb(255, 255, 0)
    color = random.choice(colors)

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(1, 300)

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for j in range (4):
        t.forward(length)
        t.right(90)

    t.end_fill()

window = turtle.Screen()
window.mainloop()


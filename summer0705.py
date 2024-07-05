# import random
# lista = []
# for i in range(i, 50):
#     lista[i] = random.randint(1 , 6)

# j = int(input(""))

# count = 0
# for i in range (50):
#     if j == lista[i]:
#         count += 1

# print(count)



# import random
# dice = [random.randint(1,6) for i in range(50)] #리스트 컴프레션을 이용한 정답 코드 

# while True:
#     num = int(input(""))
#     if not (1 <= num <= 6):
#         print(" error")
#         continue
#     print (num)
#     break

#08. 2차원 리스트의 기초 
# num = [10, 20, 30], [40, 50, 60]
# num[0][2] = 1
# print(num[0])

# num2 = [[10,20,30], [10,20,30]]
# print(num2)

# slist1 = ["LOve", "like", "excellent", "spuerpower"]
# slist2 = [["python", "C programming"] ,["java", "Kotlin"]]
# print(slist1[0][0])
# print(slist2[1][0])

# heroes = [input(": ") for i in range(5)]
# print(heroes) 리스트 컴프리헨션 

# heroes2 = input(" : ", ).split(" ")
# print(heroes2) 요것도 리스트로 저장된다.

# for i in [1,2,3,4,5]:
#     print(i, end=" ")
# print()
# for i in "string":
#     print(i, end=" ")
# print()
# for i in range(5):
#     print(i, end=" ")
# print()
# list1 = [10, 20, 30, 40, 50]
# # for i in list1:
#     # print(i, end=" ")
# for i in range(len(list1)):
#     print(f"{i} : {list1[i]}", end=" ")

# king_table = []
# for i in range (4):
#     king = input("조선시대 왕 순서 구절을 입력하시오: ")
#     king_table.append(king)

# print(king_table)
# count = 1
# for i in king_table:
#     for j in i :
#         if j == "광":
#             print("광해군")
#         elif j == "연":
#             print("연산군")
#         elif count in [1, 7, 14, 16, 21, 22, 23]:
#             print(j + "조")
#         else:
#             print(j+"종")
#         count += 1

# import random
# lista = [random.randrange(1, 101) for i in range (30)]
# # print(lista)

# i  = 0
# count = 0
# k = 50
# while i < 30:
    

#     if lista[i] > k:
#         count += 1
        
#     i += 1    


# print(count)

# import random
# # *참고 
# # -리스트 안에 리스트 만들기 
# mlist = [[0] *3 for i in range (5)]
# print(mlist)
# mlist2 = [[random.randint(1, 6) for i in range(5)] for i in range(3)]
# print(mlist2)

# import random
# quotoes = []
# quotoes.append("꿈을 지녀라. 그러면 어려운 현실에서도 빛을 잃지 않을 것이다.")
# quotoes.append("세상을 살아감에 있어 분노보다는 사랑을 믿으며 살아가는 것이 현명하다.")
# quotoes.append("처음이 쉬우면 분명 중간이나 끝은 어렵게 다가올 것이기에, 늘 올바름을 추구해야 한다.")
# quotoes.append("사람의 마음속에는 언제나 선과 악이 공존하며 그것을 선택하는 것은 자기 자신이다. ")
# quotoes.append("옳곧게 살아라, 사람답게 태어나서 짐승으로 살다 죽지 말아야 한다.")
# dailyQuotes = random.choice(quotoes)
# print("#"*20)
# print("---" + "오늘의 명언")
# print("#"*20)
# print()
# print(dailyQuotes)

import turtle
t = turtle.Turtle()
# t.speed(0)
# t.width(3)
# length = 10
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# while length < 500:
#     t.fd(length)
#     t.pencolor(colors[length%6])
#     # %6 은 그냥 0부터 5까지 중 하나가 나온다는것이고 이는 위에 있는 칼라 5개 0 1 2 3 4 5
#     # 즉 인덱스 값이 변해도 나머지 연산자의 결과는 범위 지정이 되있기에 랜덤으로 인덱스가 돌아간다. 
#     t.rt(89)
#     length += 5

# window = turtle.Screen()

positions = [0,0, 'green'], [-120, 0, 'Yellow'], [60, 60, 'red'], [-60, 60, 'black'], [-180, 60, 'blue']
t.pensize(5)
for x, y, c in positions:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c)
    t.circle(60)
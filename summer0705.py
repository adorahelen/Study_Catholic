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

# import turtle, random
# t = turtle.Turtle()
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

# positions = [0,0, 'green'], [-120, 0, 'Yellow'], [60, 60, 'red'], [-60, 60, 'black'], [-180, 60, 'blue']
# t.pensize(5)
# for x, y, c in positions:
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color(c)
#     t.circle(60)

# temp_list = [0, 10, 20, 30]
# vapor_list = [4,8,9.4,17.3,30.4]

# va = float(input(" : "))
# temp = int(input())

# if tp in temp_list:
#     hum = (va/vapor_list[temp_list.index(temp)]*100)
#     print(hum)

# tv_list = [[0, 4.8], [10, 9.4], [20, 17.3], [30, 30.4]]
# a = int(input())
# floatttt= float(input())
# if a in tv_list:
#     reslut = (floatttt/tv_list[a][1]*100)
#     print(reslut)


# tv_list = [[0, 4.8], [10, 9.4], [20, 17.3], [30, 30.4]]
# a = int(input())
# floatttt= float(input())

# for i in tv_list:
#     if a in i :
#         reslut = (floatttt/i[1])*100
#         print(reslut)

# for t, v in tv_list:
#     if a == t:
#         reslut1 = (floatttt/v)*100
#         print(reslut1)


# backet = ["치약" , "샴푸", "린스", "주방세제", "키친타올", "칫솔"]

# #code a
# a = input()
# backet.insert(a, random.randrange(1, 6))
# b = input()
# if b in backet:
#     backet.remove(b)
# c = input()
# backet.insert(c, random.randrange(1, 6))
# print(backet.index(c))

# backet = reversed(backet)
# d = backet[len(backet)]
# del[backet[len(backet)]]
# print(d)

# #code b
# a = input(" : ")
# n = random.randint(0, len(backet))
# backet.insert(n, a)
# print(backet) 

# b = input(" : ")
# if b in backet:
#     backet.remove(b)
# else:
#     print(-1)
# print(backet)

# c = input(" : ")
# if c in backet:
#     print(f" {c} in {backet.index(c)+1} is ")
# else:
#     print(-1)

# backet.sort(reverse=True)
# print(backet)

# print(backet.pop())


# import random
# computer = [random.randint(1, 6) for i in range(5)]
# user = [5]
# count = 0
# for i in range (5):
# # first 3 next 2 
#     human = input()
#     if human in "왼쪽":
#         human = 1
#     elif human in "가운데":
#         human = 2
#     elif human in "오른쪽":
#         human = 3
#     else: print(-1)

#     human2 = input()
#     if human2 in "상단":
#         human2 = 4
#     elif human2 in "하단":
#         human2 = 5
#     else: print(-1)


#     if human == 1 and human2 == 4: #왼쪽 상단
#         user = 3
#     elif human == 1 and human2 == 5: #왼쪽 하단
#         user = 4
#     elif human == 3 and human2 == 4: #오른쪽 상단
#         user = 5
#     elif human == 3 and human2 == 5: #오른쪽 하단
#         user = 6
#     elif human == 2 and human2 == 4: #가운데 상단
#         user = 1
#     elif human == 2 and human2 == 5: #가운데 하단
#         user = 2
#     else : print(-1)

   

#     user[i] = user
    
# #     if user == computer:
# #         print(" 성공 ")
# #         count += 1
# # print(count)


# centerUP = 1
# centerDW = 2
# LeftUP = 3
# LeftDW = 4
# RightUP = 5
# RightDW = 6

# for i in range (5):
#     if user[i] == computer[i]:
#         count += 1
#         print("성공")

# print(count)


# import random
# goal = ["왼쪽 상단","왼쪽하단", "가운데 하단", "가운데 상단", "오른쪽 하단", "오른쪽 상단"]
# goal2 = ["왼쪽", "오른쪽", "가운데"]
# i, cnt = 0, 0
# while i < 5: #패널티킥 5번 
#     com = random.choice(goal)
#     while True:
#         me1 = input("왼쪽, 오른쪽, 가운데 중 하나를 입력해라")
#         if me1 in goal2:
#             break
#         else:
#             print("다시 입력해라")
#     me2 = input("상단 또는 하단 입력")
#     # me = me1 + " " + me2 
#     me = f"{me1} {me2}"
#     if com == me:
#         print("패널티킥 실패")
#     else: 
#         print(f"{com}, {me}, 패널티킥 성공")
#         cnt += 1
#     i +=1
# print()
# print(cnt)

#가위, 바위, 보 프로그램을 만든다. 

# import random
# goal = ["가위", "바위", "보"]
# goal2 = ["가위", "바위", "보"]
# com = random.choice(goal)
# me1 = 0

# while True:
#     me1 = input("가위바위보중 하나를 입력해라")
#     if me1 in goal2:
#         break
#     else:
#         print("다시 입력해라")
    

# while True:
#     if me1 != com:


import random
srp = ['가위', '바위', '보']
random.shuffle(srp) 
my_srp = com_srp = '가위'
while my_srp == com_srp:
    com_srp = random.choice(srp)
    print(com_srp)
    while True:
        my_srp = input("가위, 바위, 보 중 하나를 입력: ")
        if my_srp in srp:
            break
        else:
            print("잘못 입력 하였습니다. 다시 입력해주세요")
    if my_srp == com_srp:
        print("비겼습니다. 다시합니다. ")
    elif my_srp=="가위" and com_srp=="보"or my_srp=='바위' and com_srp=="가위"...
        print("당신이 이겼습니다.")
    else:
        print("당신이 졌습니다.")
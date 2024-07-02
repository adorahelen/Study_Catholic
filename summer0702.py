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


import random
score = 100
count = 0
room = random.randrange(1, 4)

while True:
    num = int(input(" 방번호를 입력하시오 : "))
    if not 3>= num >= 1:
        print("Error")
        continue
    if num == room:
        print("범인를 잡았습니다.")
        break

    else: 
        print("그 방엔 범인 없어용")
        score -= 10
        print(score)
        if score <= 0:
            break
        count += 1
        if count == 2:
            print("초기화")
            room = random.randrange(1,4)
            count = 0

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

print("게임 끝")
print(f"{score} 점수 스코어임")
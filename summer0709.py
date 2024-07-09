# import random
# def apple ():
#     lista = []
#     for i in range (20):
#         lista.append(random.randint(1, 20))
        
#     return lista
    
# a = apple()

# def babana(a):
#     for i in range (20):
#         print(f"    {a[i]}", end="")
#         if i == 9: print("\n")
#     print("\n")


# babana(a)

# def melon(a):
#     sum = 0
#     sum2 = 0
#     for i in range (20):
#         sum += a[i]

#     print(sum)
#     k = len(a)
#     print(sum/k)

# melon(a)

# def calcla ():
#     result = 3.15 ** 2
#     return result

# r = float(input(""))
# a = int(input(" : "))
# area = calcla()
# print(area)
# name = 1

# def greet(name, msg = "asads"):
#     print(name + msg) 가능

# greet("asdasddddddddddddddddd")


# def greet(msg = "asads", name): 불가능
#  주의***디폴트 매개변수 다음애 non 디폴트 매개변수가 올 수 없다.
#     print(name + msg)

# greet("asdasddddddddddddddddd")

# 디폴트 매개변수 (인수)
# -디폴트 매개변수는 매개변수에 기본값을 설정한 것 
# 호출할 때 디폴트 매개변수 위치에 해당 인수값 생략이 가능


fun1 (y = 7, z= 2, x= 1) 가능
fun2 (5, z= 10, y=20) 가능
fun3 (y= 10, 4 , z = 1) 불가능 
위치 인수가 키워드 인수 뒤에 올 수 없음 섞어서 쓴다면
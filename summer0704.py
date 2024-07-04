# # n = int(input())
# # for i in range(1, 10):
# #     print(f"{n} * {i} = {n*i}")

# #7장 리스트 
# # heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
# # answer = [0,0]
# # jaesibal =[1,1,4]
# # numbers = [7 ,12, 33, 777]
# # print(heroes)
# # print(answer)
# # print(jaesibal)
# # print(numbers)

# # count = 1444
# # jaesibal[1] = count
# # print(jaesibal[2])

# lista = ['영어', '수학', '사회', '과학']
# print(lista) 
# print(lista[0])
# print(lista[0][1])
# print(lista[2][1])

# cat = []
# cat.append("사과")
# cat.append("포도")
# cat2 = ['오렌지']
# cat2.append("포도")
# cat2.append("사과")
# print(cat)
# print(cat2)

# cat[1] = "바나나"
# print(cat)
# cat2[2] = "바나나"
# print(cat2)
# # cat2[3] = "체리"
# # print(cat2)
# # 없는, 선언해 놓지 않은 경우 접근 및 참조 불가능, but apeend는 ㄱㅊ

# alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# print(alist[2])
# print(alist[2:3])
# print(alist[2:5])
# print(alist[:5])
# print(alist[5:])
# print(alist[:])
# blist = alist #단순히 blist가 alist를 참조
# clist = alist[:] #새롭게 만들어지는 방법
# blist[0] = 'A'
# print(blist)
# clist[0] = 'Z'
# print(clist)

# print(alist)


# list1 = [1, 3.14, True, 'String', [1,2,3], alist]
# print(list1)
# alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# i = 0
# for i in range (i, len(alist)):
#     print(alist[i], end=" ")

# blist = alist[:]
# alist[2:5] = 'k'

# i = 0
# print("")
# for i in range (i, len(alist)):
#     print(alist[i], end=" ")
# print(alist)
# alist[2:5] = ['c', 'd']
# blist[2] = ['c', 'd']
# print(alist)
# print(blist)

# cart = ['사과', '섬유유연제', '화장지', '치약']
# cart.append('앙멀')
# print(cart)
# cart.insert(1, '간잔지')
# print(cart)
# cart.insert(0, "라아멘")
# print(cart)
# cart.insert(len(cart), '칫솔')
# print(cart)

### 리스트 정리
# 리스트 생성 = [] 공백리스트 생성, 자꾸 까먹지 말것
# 리스트 요소 접근 = [1,2,3]
# 리스트 = list(): 공백리스트 생성, list() 함수는 다른 시퀸스를 리스트로 변경하는 것이 가능
# 즉 리스트 생성은 두가지, 공백리스트 생성 or 리스트 함수 사용
# alist = []
# blist = list()
# clist = list("tmxmfld")
# dlist = list(range(10))
# => 이게 하나 씩 리스트에 들어가는게 시퀸스를 리스트로 변환한다는 말임
# print(alist, blist, clist, dlist)

##리스트에 요소 추가하는 법
# 리스트 .append(요소) 요소를 리스트 마지막에 추가
# 리스트 .insert(인덱스, 요소): 요소를 인덱스 위치에 삽입(추가)
# 리스트 .extend(리스트2) : 리스트 마지막에 리스트 2 요소를 추가 (또 다른 리스트를 리스트안에 넣는것도 가능함)
# * 덧셈 연산자 사용으로 리스트 까리 더해서 새로운 리스트를 병합하여 새로운 리스트 생성이 가능하다. 
# alist = [1,2,3,4,5,5,]
# vlist = ["ㄴㄹㄻㄴㅁ"]
# dlist = list("asfassfas")
# dlist.extend(alist)
# print(dlist)
# elist = alist + vlist + dlist
# print(elist)

#리스트 슬라이싱 : 문자열 슬라이싱과 동일
#리스트 요소 수정 변경은 인덱스와 대입연사자를 사용한다.
# 주의 1: 슬라이싱 범위로 지정하면 해당 범위의 요소들이 변경되고, 인덱스로 하면 요소값이 변경된다. 
# 주의 2: 슬라이싱의 결과는 리스트 

#삭제시 인덱스가 아니라 요소값을 넣어서 삭제하는 .remove, 따라서 조건문으로 remove() 사용
# cart = ['사과', '세제', '화장지', '치약']
# cart.remove('화장지')
# print(cart)
# if '라면' in cart : 
#     cart.remove('라면')
# print(cart)
# cart.remove("sdasd")

alist = [1,2,34,5,6,7,7,78,8,89,]
del alist[3]
print(alist)
del(alist[3])
print(alist)
del(alist[2:6])
print(alist)

alist = ['사과', '삭제', '세제']
item = alist.pop()
print(alist, item)
item = alist.pop(0)
print(alist, item)
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

# alist = [1,2,34,5,6,7,7,78,8,89,]
# del alist[3]
# print(alist)
# del(alist[3])
# print(alist)
# del(alist[2:6])
# print(alist)

# alist = ['사과', '삭제', '세제']
# item = alist.pop()
# print(alist, item)
# item = alist.pop(0)
# print(alist, item)

# 리스트 요소 삭제
# 리스트.remove(요소) : 리스트에 있는 요소를 찾ㅈ아 삭제(단 동일한 것이 있더라도 첫번째만 삭제하고 없으면 에러 발생)
# del 리스트 [인덱스] : 인덱스에 해당하는 요소를 삭제, del(리스트[인덱스])같이 함수 형태로도 사용 가능
# del 리스트 [인덱스1 : 인덱스2] : 두 인덱스 사이에 있는 요소들을 삭제
# 리스트 [인덱스 1 : 인덱스2] = [] 사이에 있는 요소들을 공백으로 치환 즉 삭제
# 리스트 .pop() 리스트 마지막 요소를 반환하면서 삭제
# 리스트 .pop(인덱스) d인덱스 해당하는 요소를 반환하면서 삭제
# 리스트. clear () : 리스트의 모든 요소를 삭제, del 리스트[:], 리스트[:] = [], 리ㅣ스트 = []
# 주의 : del 리스트라고 하면 리스트 변수 자체가 소멸한다. 

# cart = ['사과', '섬유유연제', '화장지', '치약']
# cart[1:3] = [] 
# print(cart)
# cart.clear()
# print(cart)
# cart = ['사과', '섬유유연제', '화장지', '치약']
# print(cart)
# del cart[:]
# print(cart)
# cart = ['사과', '섬유유연제', '화장지', '치약']
# cart[:] = []
# print(cart)
# cart = ['사과', '섬유유연제', '화장지', '치약']
# print(cart)
# cart= []
# print(cart)
# cart = ['사과', '섬유유연제', '화장지', '치약']
# print(cart)
# del cart
# print(cart)

#리스트에서 항목 탐색하기 

#리스트 index(요소) : 요소가 몇 번 인덱스에 있는지 인덱스 값 반환 (동일한 요소 있어도 첫 번째 찾은 요소 인덱스만 반환)
#해당 요소가 없으면 에러 
# 리스트.index(요소, start, end) : start ~ end -1 사이의 범위를 해당요소 찾아 인덱스 위치 반환 
# cart = ['사과', '섬유유연제', '섬유유연제', '섬유유연제', '화장지', '치약', '린스']
# print(cart.index('화장지'))
# if '라면' in cart:
#     print(cart.index('라면'))
# print(cart.index('화장지', 3,6))
# print(cart.index('린스', 3, len(cart)))

#신나는 리스트 정렬하기 sort 가즈아 오름차순 나이 올라감 내림차순 나이 내려감, sort 써도 나중에는 직접 짜야함 기본적으로는 오름차순
# new_list = sort(list), reverse = True 하면 내림차순, sorted 함수 쓰면 정렬된 새 리스트 나옴
#리스트.sort : 정렬하는데 사용, 원본리스트를 변경, 오름차순으로 정렬
#리스트.sort(reverse=True) : 내림차순 정렬
#리스트.reverse(): 리스트의 요소 순서를 역순으로 변경, 정렬이 아님
# list2 = list1.sorted() 틀림
# list2 = sorted(list1)  이런식으로 사용
# .sort() 한후후에 리스트 .reverse() 해도 내림차 정렬 가능

# cart = [29, 39, 19, 29, 939,3,4, 14444]
# cart2 = cart[:]
# cart3 = cart[:]
# cart.sort()
# print(cart)
# cart2.sort(reverse=True)
# print(cart2)
# c1 = sorted(cart3)
# print(c1)
# c2 = sorted(cart3, reverse=True)
# print(c2)
# cart3.reverse()
# print(cart3)

# list.count
# list2 = list.copy
# list2 = list + []
# list2 = list[:]
# 주의 : 리스트2 = 리스트 : 동일 내용으로 새로운 이름을 추가, 원본 리스트에 새 이름 추가한거임 (바로가기)

# 리스트 컴프리헨션 
# 리스트 = [저장요소 반복문] : 중간에 콤마가 들어가지 않고 공백이 들어감 [밑에 나온 형태]
# 리스트 = [random,randint(1, 10) for i in range(10)] : 10 개의 값 추출 되어 요소로 저장돠면서 리스트 생성 

import random
list1 = [i for i in range(10)]
print(list1)
print(list1[3])
print(list1.count(3))
print(list1.count(13))
list2 = [random.randrange(1, 11) for i in range(10)]
print(list2)

list3 = []
for i in range(10):
    list3.append(random.randint(1, 10))
print(list3)
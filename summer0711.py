# s1 = {10, 20, 30, 40, 50, 60, 70}
# s1.discard(80)
# s1.discard(30)

# print(s1)#순서가 뒤죽 박죽 나오는 이유는, 집합 자료형이 순서가 없기 때문이다. 

# if 80 in s1:
#     s1.remove(80)

# s1.remove(40)
# print(s1)
# s1.clear()
# print(s1)

# list1 = [10, 10, 30, 20, 40, 30, 70, 90, 100, 90]
# s2 = set(list1)
# print(s2)

# s3 = s1 | s2
# s4 = s1 & s2
# s5 = s1 - s2

# s3 = s1.union(s2)
# s4 = s1.intersection(s2)
# s5 = s1.difference(s2)
# print(s3)
# print(s4)
# print(s5)

# import random

# def match(c, m):
#     if c == m:
#         return "비켰네"
#     elif match_table[c] == m:
#         return "졌네"
#     else:
#         return "이겼다아아아아앙"
    
# dic = {1:"가위", 2: "바위", 3:"보"}
# match_table = {"가위" : "보", "바위" : "가위", "보" : "바위"}
# computer = dic[random.randint(1,3)]

# while True:
#     computer = dic[random.randint(1,3)]
#     print(computer)
#     while True:
#         mine = input("가위, 바위, 보 : "  )
#         if mine in dic.values():
#             break
#         else:
#             print("다시입력햇라")
#         result = match(computer, mine )
#         print(result)
#         if result == "비겼네":
#             print("re갬")
#         else:
#             break

# planet_dict = {"수성" : 91700000, "금성" : 4140000, "화성":78400000, "목성":628700000, "토성":1277400000, "천왕성":275400000, "해왕성":4347400000}
# planet = input("해성 이름: ")
# speed = int(input("이동석도(kn/h): "))
# distance = planet_dict[planet]
# time = distance/speed
# year = int(time) // (365*24)
# month = int(time - (year*365*24)) // (30*24)
# day = int(time- (year*365*24) - (month*30*24)) // 24
# hour = int(time-(year*365*24) - (month*30*24) - (day*24))
# print(f"이동시간: 약 {time}")
# print(f"이동시간 : 약 {year}, {month}, {day}, {hour}")

# def count_descendant (d):
#     d_dict = {}
#     for n in d:
#         if n in d_dict:
#             d_dict[n] += 1
#         else:
#             d_dict[n] = 1
#     print(d_dict)
#     cal_rate(d_dict)

# def cal_rate (d):
#     rate = (d['RR'] + d['Rr'] +d['rR' / d['rr']])   
# def make_descendant
# import random
# descendant = []
# for n in range(100):

# awards = []
# awards.append({'이름' : '팀 버너스리', '수상년도':2016, '국적':"영국", '대표산업':"헬스케어"})
# awards.append({'이름' : '팀 어벤져스', '수상년도':2024, '국적':"대구", '대표산업':"법률 서비스 플랫폼"})
# awards.append({'이름' : '팀 암행어사', '수상년도':2024, '국적':"하양", '대표산업':"암표 검출 인공지능"})
# awards.append({'이름' : '팀 화석연료', '수상년도':2024, '국적':"경산", '대표산업':"심리 치료"})
# awards.append({'이름' : '팀 나눔플러스', '수상년도':2021, '국적':"제주", '대표산업':"초록 우산 어린이 재단 설립"})

# for award in awards:
#     print(award)

# print("=========수상자 명단 ========")
# for award in awards:
#     print(award['이름'])

# print()
# print("===수상한 년도===") #수상한 년도 얼마나  수상하게 살았는지 ㅋ
# #ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# for award in awards:
#     if award['수상년도'] >= 2020:
#         print(award['이름'], award['수상년도'])
# print()
# print("===수상자 국가===")
# national = set()
# for award in awards:
#     national.add(award['국적'])
# print(national) 
# import random

# Sdict = {}
# for i in range (1, 21):
#     Sdict = {f"str{i}" : random.randint(0, 100)}
#     # print(Sdict)
#     # print(Sdict)

# cnt = 0
# sum1 = 0

# for i, j in Sdict.items():
#     print(i, j)
#     sum
#     if  j> 70
#     cnt + 1
    
#     print

# import random

# Sdict = {}
# for i in range(1, 21):
#     Sdict[f"str{i}"] = random.randint(0, 100)  # Add key-value pair to the dictionary

# cnt = 0
# sum1 = 0

# for key, value in Sdict.items():
#     print(key, value)
#     sum1 += value  # Accumulate the sum of values
#     if value > 70:
#         cnt += 1  # Increment the count if the value is greater than 70

# print(f"Sum of all values: {sum1}")
# print(f"Count of values greater than 70: {cnt}")

# 한 판매회사에서 판매실적 점수와 고객평가 점수를 통해 우수한 제품을 선발한다
# lilili = {"세제", "비누", "락스", "칫솔", "샴푸", "치약", "린스", "샴푸", "치약", "로션"}
# 여기서 고객평가 점수가 4점ㅇ 이상인 제품은 샴푸, 치약, 린스

# lilili = {"세제", "비누", "락스", "칫솔", "샴푸", "치약", "린스", "샴푸", "치약", "로션"}
#판매실적 점수, 고객 ㅠㅕㅇ가점수 

# product = {"세제", "비누", "락스", "칫솔", "샴푸", "치약", "린스", "샴푸", "치약", "로션"}
# sale = {"세제", "비누", "락스", "칫솔"} # 판매 실적 4점 이상
# custom = {"세제", "비누", "락스"}

# a = sale&custom
# print("우수제품", a)
# b = product - (sale | custom)
# product("판매중지 제품 ", b)

#어느 학급의 학생 수는 34명이고, 국어, 영어, 수학 시험을 봤다.
#학생들의 아이디는 str1 ~ str34
# 과목별 점수는 0~100
#key 아이디이고, Value 는 [국어, 영어, 수학]의 형태로 각 과목별 점수를 갖는 리스트를 사용한다.
# import random

# Sdict = {}
# Sdict2 = {}
# Sdict3 = {}
# sumDict = {}
# for i in range(1, 34):
#     Sdict[f"stud{i}"] = random.randint(0, 100)  # Add key-value pair to the dictionary

# for i in range(1, 34):
#     Sdict2[f"stud{i}"] = random.randint(0, 100)

# for i in range(1, 34):
#     Sdict3[f"stud{i}"] = random.randint(0, 100)

# for i in range(1, 34):
#     sumDict[f"stud{i}"] = Sdict.values(i) + Sdict2.values(i) +Sdict3.values(i)

# import random

# Sdict = {}
# Sdict2 = {}
# Sdict3 = {}
# sumDict = {}

# # Fill Sdict, Sdict2, and Sdict3 with random values
# for i in range(1, 34):
#     Sdict[f"stud{i}"] = random.randint(0, 100)  # Add key-value pair to the dictionary
#     Sdict2[f"stud{i}"] = random.randint(0, 100)
#     Sdict3[f"stud{i}"] = random.randint(0, 100)

# # Create sumDict with the sum of values from Sdict, Sdict2, and Sdict3
# for i in range(1, 34):
#     key = f"stud{i}"
#     sumDict[key] = Sdict[key] + Sdict2[key] + Sdict3[key]

# # Print the dictionaries
# print("Sdict:", Sdict)
# print("Sdict2:", Sdict2)
# print("Sdict3:", Sdict3)
# print("sumDict:", sumDict)

import random
classdic = {}
for i in range(34):
    classdic[f"stud{i+1}"] = [random.randint(0, 100) for i in range(3)]
print(classdic)

english = []
for i, j, k in classdic.values():
    english.append(j)
print(max(english))

average = []
for k,e,m in classdic.values():
    avg = (k+e+m) // 3
    average.append(avg)
print(avg)
print(average)

for i,j in classdic.items():
    sum1 = 0
    for k in j:
        sum1 += k
    if sum1 // len(j) == max(average):
        print(sum1//len(j))
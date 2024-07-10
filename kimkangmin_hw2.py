# 학번 : 202429332, 이름 : 김강민, 전공 : 컴퓨터공학

# 다음 조건에 맞도록 프로그램 작성하시오 (순열 문제임)
# 1. 문자 리스트에 대문자, 소문자 섞어서 저장
# 2. 랜덤으로 3개 문자 추출 (중복은 허용하지 않음)
# * print 추출한 문자 리스트 한 번 추출 => 문자 3개 출력된다.

# 3.print 순열조합으로 정렬된 리스트 출력 (6개_ 리스트의 원소)
# 4.print 순열조합으로 정렬된 문자열 출력 (6개)
# *출력시 오름차순으로 정렬 시킬 것 =>  sort(),sorted

import random
#랜덤 모듈 사용을 위한 코드

#문자 리스트를 생성하기 위한 함수
#리스트 컴프레션이 어렵기도 하고, 편한 반복문을 사용해서 작성
def firstlist():
    listOfchar = []
    for i in range(65, 91):
        listOfchar.append(random.randint(65, 90))

    for i in range(97, 123):
        listOfchar.append(random.randint(97, 122))
    
    return listOfchar
    # 2차원 리스트 선언, 반복문을 통해 대문자 / 소문자 저장
    # 배열에 대한 개념 부족으로 2차원 리스트 대입 실수 
    # 후술할 sample 함수를 사용하려면 리스트 2개가 아닌 하나에 저장 해야함

# print(listlist1) 출력 확인용



#랜덤 셔플 함수를 통해 무작위 값 추출, 함수 자체에서 중복 허용 안함
def SQLandSelect(listlist):
    return random.sample(listlist, 3)
# 3개를 골라서 반환 하는 것 까지 진행, 이를 문자로 바꾸는 것은 추후 수행



listlist1 = firstlist() #함수를 통해 리스트 생성 후 할당 
charlist1 = SQLandSelect(listlist1) # 함수를 통해 뽑은 3개만 반환
# print(charlist) 확인용, 밑에는 숫자를 문자로 바꾸는 코드
for i in range(3):
    charlist1[i] = chr(charlist1[i])
print(f"1) 추출된 문자 3개: {charlist1}")    
# 여기까지는 이상 없음 


  
# 오늘 배운 재귀함수 응용식
def lastday(chartist1):
    combinationPizza = []

    def mix(nowStateIhave, nokorimono): #현재와 남은것을 인수로 넣고
        if len(nokorimono) == 0: #남은게 없으면 추가
            combinationPizza.append(nowStateIhave)
        else: #남은게 있으면 반복문 돌려서 재귀로 진행
            for i in range(len(nokorimono)):
                add_now = nowStateIhave + nokorimono[i]
                add_nokori = nokorimono[:i] + nokorimono[i+1:]
                mix(add_now, add_nokori)

    mix("", charlist1) #시작
    return combinationPizza

result1 = lastday(charlist1) #재귀함수 돌린 결과 저장 (정렬전 print문 2번에 사용)
result2 = sorted(result1) #진짜 결과값 (정렬후 3번에 사용)
# print(result2)
 # 오름차순 정렬



print(f"2) 문자들을 조합한 요소를 갖는 리스트 출력:") 
result3 = [list(i) for i in result1]
print(result3)



print(f"3) {charlist1}(으)로 만들 수 있는 모든 문자열(정렬하여 출력함)") 
result4 = ["".join(j) for j in result2]
print(" ".join(result4))


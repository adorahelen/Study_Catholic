"""
1. 파이썬 개요
2. 변수 
3. 연산자 
4. 자료형 (기본)
5. 조건식
6. 반복문
7. 리스트
8. 함수
9. 딕셔너리 & 집합

-그래픽 모듈 정리
자바의 스윙 처럼, 파이썬은 터틀 그래픽 모듈을 제공한다.
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward() 거북이 전진
t.left() 거북이 왼쪽 회전
t.right() 거북이 오른쪽 회전
t.circle() 원그리기 
t.width() 선의 두께 
t.color() 선의 색상

사각형 그리기 
: 선그리기-90도회전하기-선그리기-90도회전하기-선그리기-90도회전하기-선그리기
*삼각형은 120도 
*육각형은 60도
*오각형은 72도
*팔각형은 45도
=> 모든 다각형 외각의 합은 360도이다.

t.beginfill() == t.color() == t.end_fill()
t.setheading : 터틀 헤드를 특정한 각도로 설정한다.
t.goto(x,y)

s = turtle.textinput("", "이름을 입력하세요")
t.write("안녕하세요." + "s" + "씨, 터틀 짱 인사드립니다.")



리스트란?
여러개의 데이터를 의미 있게 묶어서 저장하는 것
파이썬의 리스트는 시작과 끝을 표시하기 위하여 [ ] 이거 사용 안에서 , 로 분리하여 넣는다.
heroes = ["아이언맨", "토르", "헐크"]
+ 문자열 기본적으로 []

딕셔너리란? 
Key()값을 이용해 자료에 접근한다.
키와 관련된 값이 짝을 이루고 있다. { "홍길동" : "12345678", "이성게" : "라면" , }
+ 집합도 기본적으로 {}
"""
awards = []

for award in awards:
    print(award)

for award in awards: 
    if award['수상년도'] <= 1990:
        print(award['이름'], award['수상년도'])

nation = set()
for award in awards:
    nation.add(award['국적'])

'''
딕셔너리 형태로 데이터를 만들고 이를 다시 리스트로 만드는 방법은 딕셔너리 형태의 데이터를 리스트에 append( 딕셔너리 자료형 )
넣어서 만들면 된다. 

'''

planet_dict = {'수성' : 9140000, '금성': 1987855, "목성": 453212312}

planet = input("행성이름 : ")
speed = int(input(" : "))
distance = planet_dict[planet]

time = distance / speed

'''
집합의 항목을 삭제할 때는 discard 디스카드, remove 리무브, clear 클리어를 사용!
*집합도 자료의 뭈음이다, 집합은 *중복된 데이터를 가질 수 없으며, 순서가 없다. 
'''
# 딕셔너리 출력하기 위드 반복문
for i in planet_dict.keys():
    print(i)

for i in planet_dict.values():
    print(i)

for i,j in planet_dict.items():
    print(i,j)

english_dict = {}
english_dict['원'] = '하나'
print(english_dict)
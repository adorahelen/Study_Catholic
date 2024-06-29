# 학번 : 202429332, 이름 : 김강민, 전공 : 컴퓨터공학

#터틀 그래픽을 이용하여 가위바위보 게임 구현하기

import random
import turtle
#랜덤 함수 사용 및 터틀 그래픽 사용을 위한 라이브러리 포함

value = 0
com_number = 0
result = 0
com_value = 0
t = turtle.Turtle()
t.shape('turtle')
#사용할 변수 메모리 할당 및 터틀 함수를 통한 터틀 객체 생성 및 모양 지정

#s = turtle.textinput("가위바위보", "가위, 바위, 보 중 하나를 입력하세요.")

s = turtle.textinput("가위바위보","가위 바위 보 중 하나를 입력하시오 : ")
if s == "가위" : value = 1
elif s == "바위" : value = 2
elif s == "보" : value = 3
else : t.write("잘못 입력하였습니다.", False, "center", ("", 20, "bold"))
#키보드를 통해 입력받은 문자에 맞게 정수 1 or 2 or 3 할당

com_value = random.randrange(1, 4)
if com_value == 1 : com_number = "가위"
elif com_value == 2 : com_number = "바위"
elif com_value == 3 : com_number = "보"
else :  com_number = -1
# 랜덤함수에 할당된 숫자 1, 2, 3에 걸맞은 가위 바위 보를 문자열로 할당한다.
#논리 오류 캐치를 위한 else : -1


if com_number == 0: result =0
#변수에 값이 제대로 할당되지 않아 초기값이 출력될 경우 결과값으로 0을 할당
elif com_value ==1  and value ==2  : result = "나의 승리"
# 컴퓨터 가위, 나 바위
elif com_value ==1  and value ==3  : result = "컴퓨터 승리"
# 컴퓨터 가위, 나 보
elif com_value ==2  and value ==1  : result = "컴퓨터 승리"
# 컴퓨터 바위, 나 가위
elif com_value ==2  and value ==3  : result = "나의 승리"
#컴퓨터 바위, 나 보
elif com_value ==3  and value ==1  : result = "나의 승리"
#컴푸터 보, 나 가위
elif com_value ==3  and value ==2  : result = "컴퓨터 승리"

elif com_value ==2  and value ==2  : result = "무승부"
elif com_value ==1  and value ==1  : result = "무승부"
elif com_value ==3  and value ==3  : result = "무승부"
#콤퓨터 보, 나 바위
else : result = -1

# print(f"나 : {s} vs 컴퓨터 : {com_s}, 결과 : {result}")
t.up()
t.goto(0,150)
t.write(f"{result}", False, "center", ("", 25, "bold"))

t.goto(-100,-150)
t.back(100)
t.write(f"{s}", False, "center", ("", 35, "bold"))

t.fd(350)
t.write(f"{com_number}", False, "center", ("", 35, "bold"))

window = turtle.Screen()
window.exitonclick()
#이 부분은 VsCode에서 window에 turtle.Screen()을 할당하지 않으면 창이 1초만에 사라지기에 작성함


#얼추 완성했는데, 지속적으로 사용자가 가위를 입력했을때 이유불명의 무승부가 출력된다.
# 해결 : 변수명 오류 : if com_value == 1 : com_number = "가위" 라인 com_numbers로 작성
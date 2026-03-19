# Step05_Function.py

'''
    function type

    - 특정 시점에 여러 줄의 code를 일괄 실행하고자 할 때 사용한다.
    - 함수 또한 하나의 data이다(변수에 담을 수 있다)
    - 함수 안에 저장된 code를 일괄 실행하는 것을 함수를 call(호출)한다고 이야기한다.
    - 함수는 저장된 code를 다 실행하고 나면 원래 call했던 위치로 실행의 흐름이 넘어온다.
    - call했던 위치로 돌아오며 어떤 data를 반드시 가져온다.
'''

def test1():
    print("test1() 호출됨")


test1()
result1=test1()

# 매개변수가 선언되어 있는 함수
# 매개변수에 대입할 값을 전달해야지 호출할 수 있다.
def test2(arg):
    print("전달받은 내용:", arg)
    print(f"전달받은 내용: {arg}")

test2(None)
test2(10)
test2("kim")

def print_sum(num1: int, num2: int): #'변수 : type hint' 형태로 자료형을 정의할 수 있다.
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10, 20)

def print_info(name: str, addr: str):
    print(f"이름은 {name}이고 주소는 {addr}이다")

print_info("양재혁",'순천')
# keyword를 이용하여 인자(argument)를 전달할 수도 있다.
print_info(addr = "신대지구",name = '재혁')

# return 키워드를 이용하여 값을 반환할 수 있다.
def get_sum(num1: int, num2: int):
    sum = num1+num2
    return sum

result2=get_sum(11,32)

print("종료됩니다")
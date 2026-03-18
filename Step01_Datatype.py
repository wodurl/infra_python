# 한 줄 주석입니다용

"""
오레오

반가워용
"""

print("Step 01 시작")

num1 = 10
num2 = 10.1

Myname = '김구라'
Yourname = "해골"
Ourname = """
KT Cloud 인프라"""
print(type(Ourname))

#list type
#순서가 중요한 여러 개의 데이터를 관리 -> list
food1="삼겹살"
food2="닭발"
food3="냉면"
foods=["삼겹살","닭발","냉면"] 

print(foods)

#dictionary type
#순서가 중요하지 않은 여러 개의 데이터를 관리 -> dict
num1 = 1
name = "김구라"
addr = "노량진"
mem1 = {"num":1, "name":"김구라", "addr":"노량진"} 

print(mem1)

#Set type
#순서가 중요하지 않은 여러 개의 데이터를 키 값 없이 묶음으로 관리 -> set
Myset = {"빨강사탕", "노랑사탕", "초록사탕"} 

print(Myset)

#Function type
#함수도 데이터 타입의 일종이다 -> 변수처럼 사용 가능
def store(): 
    print("냉장고 문을 연다")
    print("물건을 넣는다")
    print("냉장고 문을 닫는다")
    
#Function 타입은 필요한 시점에 호출하면 된다.
#함수를 실행하고 return할 때, 반드시 어떤 데이터를 가지고 온다.
store()
d = store()

#참과 거짓을 나타내는 데이터 타입 -> "bool"
isMan=True
isWoman=False
isDifferent=True
isRun=False

#어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶다면? "None"
a = None
print("필요할 때 값 넣기")
a = 'test'


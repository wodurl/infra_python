# Step06_Tuple.py

'''
    - Tuple
    1. list type과 유사
    2. 읽기 전용(수정, 삭제 불가)
    3. 기능이 적기 때문에 속도 처리가 빠르다
'''

# "one", "two", "three" 3개의 데이터를 tuple에 순서대로 담고
# 그 객체의 참조 값을 tuple type tuple1이라는 변수에 담기
tuple1: tuple = ("one", "two", "three")
result1 = tuple[0]
result2 = tuple[1]
result3 = tuple[2]

# Read Only이므로 수정, 삭제가 불가능하다
# del tuple1[0]
# tuple1.remove(0)

# 방 1개짜리 tuple type을 만들 때는 주의
tuple2 = ("김구라",)
# 뒤에 ,를 붙이지 않으면 그냥 문자열로 판정

# 괄호 없는 튜플 생성
tuple3 = 10, 20, 30

# tuple에 저장된 값을 여러 변수에 나누어 담기
a, b, c = tuple3

# 두 변수에 있는 값을 서로 바꾸려면?
first = "girl"
second = "boy"

'''
temp = first
first = second
second =temp
'''
# 위의 세 줄을 아래와 같은 코드로 해결할 수 있다.
first, second = second, first 

print("종료")
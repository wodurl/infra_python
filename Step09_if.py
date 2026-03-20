# Step09_if.py

'''
    임의의 숫자를 입력받아서 입력한 수가 양수이면 "양수입니다."를 출력하고자 한다면?
'''

# 숫자를 입력받는다.
input_num: int = int(input("임의의 정수 입력: "))

if input_num > 0:
    print("입력한 수는 양수입니다.")

# 입력한 수가 짝수면 짝수입니다. 홀수면 홀수입니다를 출력하기
if (input_num % 2) == 0:
    print("짝수입니당")
else:
    print("홀수입니당")

print("종료.")
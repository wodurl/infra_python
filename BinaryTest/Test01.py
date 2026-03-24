# BinaryTest/test01.py

# Python에서 2진수 다루기

# 2진수를 10진수로 만들 때 prefix 로 0b
num1 = 0b1010

result = num1 + 5
print(result)

# 10진수를 2진수로 변환
num2 = 150
result2: str = bin(num2) # bin() 함수 호출하면서 10진수를 넣어주면 2진수 숫자 값이 나온다.
print(result2)

print("---------------")
line = "abced12345"
print(line[5:10])   # 문자열에도 인덱스 활용 가능. 5번 인덱스 이상, 10번 인덱스 미만의 문자열 얻어내기

# result2 문자열 (0bxxxxxxx) 에서 0b를 제외한 순수 2진수 형태의 문자열만 얻어내기
print(result2[2:])
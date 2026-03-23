# test05.py

source = '11110000'
# source가 2진수라는 것을 전달하면 알아서 정수 형태로 바꾸어줌
print(int(source, 2))

source2 = '11110003'

# set() : source 문자열 하나하나를 set로 만듬 -> {"0","1"}로만 이루어짐
# .issubset() : . 왼쪽의 집합이 인자의 집합에 포함되나?
result1 = set(source).issubset({'0','1'})
result2 = set(source2).issubset({'0','1'})
print(f"{source}가 0과 1로만 되어있는지 여부: {result1}")
print(f"{source2}가 0과 1로만 되어있는지 여부: {result2}")
print(f"{source}가 8자리 이상인지 여부: {len(source)>=8}")
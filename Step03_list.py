"""
List의 특징
1. 순서가 있다
2. 여러 타입의 데이터를 섞어서 저장할 수 있다
3. 값 변경 가능
"""

names = ["김구라","해골","원숭이"]
nums = [10, 20, 25]

# 여러 데이터 타입을 섞어서 담는다(일반적이진 않음)
datas=[10,"xxx", True]

nums.append(40)

# len() built-in 함수를 사용하여 list의 길이를 알아낼 수 있다.
nums_len = len(nums)

# 인덱스에 의한 참조
name0 = names[0]

# 인덱스를 이용하여 삭제
del names[0]

# 값을 이용하여 삭제
names.remove('원숭이')

# 맨 마지막 index를 삭제하며 값 가져오기
nums.pop()
result = nums.pop()

print("종료합니다")
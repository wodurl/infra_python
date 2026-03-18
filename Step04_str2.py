"""
json 문서 형식
{
    "name":"양재혁",
    "addr":"순천",
    "food":["초밥","피자"]
}
"""

# json 모듈 import 하기
import json

# info는 str type이긴 하나 문자열이 특별한 방식(json)을 띄고 있다.
info = '''{
    "name":"양재혁",
    "addr":"순천",
    "food":["초밥","피자"]
}'''

# result는 str(json 형식)의 문자열이 python의 dict로 변경된 값을 가지고 있다.
result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["food"])
print(result["food"][0])
print(result["food"][1])

result2 = json.dumps(result)

print("종료됨")
# Str type에 대해 알아보자 (중요)

# 양쪽에 공백이 포함되가나 포함될 가능성이 있는 문자열이 있다고 가정, 공백을 제거하려면?
text = "   Cloud Infra"
result1 = text.strip()

# .으로 분리하기
myIp = "192.168.0.2"    
result2 = myIp.split(".") # 나눈 결과는 list에 반환

# join 다시 합치기
result3 = ".".join(result2)

# 특정 문자열 찾아 대체하기 
result4 = "hello, mimi!".replace("mi", "ma")

result5 = "python".upper()
result6 = "PYTHON".lower()
print("제거합니다")
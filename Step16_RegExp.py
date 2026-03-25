# Step16_RegExp.py
'''
    정규표현식 (Regular Expression) 에 대해 알아보자
    정규표현식은 모든 언어에서 존재.
'''

# 우리는 어떤 문자열을 검증하거나, 혹은 특정 문자열에서 원하는 단어나 기호를 찾아야 할 때가 있다.

import re # Python 제공 정규표현식 객체

# 대상 문자열에서
data:str = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%97%AC%EC%8A%A4%EC%9E%A5&ackey=cnmteg2e"

# "a"라는 정규표현식에 매칭되는 모든 문자열을 찾아서 list에 담아 리턴
result = re.findall(r"%..", data)

print(result)

# 대상 문자열 2
text:str = "Contact: 010-1234-9876입니다"

m_obj = re.search(r"010-[0-9]{4}-[0-9]{4}", text)

print(m_obj)
print(m_obj.group())
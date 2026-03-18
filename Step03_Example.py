"""
회원 한 명의 정보는 번호, 이름, 주소로 이루어져 있다.
그리고 그러한 회원이 여러명이다
여러 명의 회원 목록을 하나의 묶음으로 순서대로 관리하고 싶다면?
"""

# 3명의 회원 정보를 각각 dict에 담은 다음 그 dict를 list에 담는 코드를 작성
member1 = {"num": 1, 'name': 'yang', "addr": 'suncheon'}
member2 = {"num": 2, 'name': 'kim', "addr": 'seoul'}
member3 = {"num": 3, 'name': 'lee', "addr": 'busan'}

total_mem = [member1, member2, member3]

a = total_mem # [member1, member2, member3]
b = total_mem[0] # {"num": 1, 'name': 'yang', "addr": 'suncheon'}
c = total_mem[0]["num"] # 1
d = total_mem[0]["name"] # "yang"

print('종료합니다')
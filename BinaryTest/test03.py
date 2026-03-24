# BinaryTest/test03.py

# 비트연산 or, xor, not
a=0b1010
b=0b1100

# bit or 연산
print(bin(a|b))

# bit xor 연산
'''
    xor 진리표
    0, 0 -> 1
    0, 1 -> 0
    1, 0 -> 0
    1, 1 -> 1
'''
print(bin(a^b))

# bit not 연산
print(bin(~a))  # 1010 -> 0101
# 1100은 12, not 연산 ~12는 -(12+1)
print(bin(~b))  # 1100 -> 0011
print(bin(~a & 0xf)) # 0b101(0101)
# python에서 int는 비트 길이가 무한대, not 연산하게 되면 무수히 많은 1이 생성됨.
# 그러므로 ~a = -(a + 1) 공식을 활용함
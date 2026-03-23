# BinaryTest/test02.py

a=0b1010
b=0b1100

# a와 b를 비트 AND 연산(자리수 별로 모두 1일 때 결과가 1)
print(a & b)
print(bin(a & b))

info = 0b1111_1111_1111_0000
print(bin(info))
data1 = 0b1100_0011_1010_0000
data2 = 0b1100_0011_1010_0001
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100

data5 = 0b1111_0000_1010_1111

print(bin(info & data1))
print(bin(info & data2))
print(bin(info & data3))
print(bin(info & data4))
print(bin(info & data5))
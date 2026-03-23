# BinaryTest/test04.py

ip_addr = input("ip 주소 입력(ex: 192. 168.0.1): ")

# .으로 분리해서 리스트 형태로 저장
ip_pars = ip_addr.split(".") # split()은 str 타입의 내장 함수

print(ip_pars)

# 빈 배열
binary_parts = []

for item in ip_pars:
    # :08b는 뒤에서 부터 읽으면 b(2진수)로 변환하되 총 8자리로 변환하고 빈 곳은 0으로 채움
    print(f"{int(item):08b}")
    # 2진수 8자리로 구성된 값을 빈 배열에 추가(append)
    binary_parts.append(f"{int(item):08b}")

print(binary_parts)
# 리스트에 저장된 각각의 아이템과 "."을 join한다(split의 반대 동작)
result = ".".join(binary_parts)

print(result)

print(f"입력한 ip: {ip_addr}")
print(f"2진수 변환한 ip: {result}")
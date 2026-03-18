nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", 'choi']

# 리스트에 들어있는 데이터를 앞에서부터 순서대로 참조하며 동작을 할 일들이 많이 발생
for item in names:
    print("names를 순서대로 출력중")
    print(item)

r1 = range(5) # >>> [0, 1, 2, 3, 4]
r2 = range(10) # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(r1, r2)

for item in range(5):
    print(item)

result2 = range(len(names))

for i in range(len(names)):
    print("list와 그 index를 함께 출력")
    print(i, names[i]) # 반복문을 돌며 i에 들어있는 인덱스를 이용하여 순서대로 참조

print('종료합니당')
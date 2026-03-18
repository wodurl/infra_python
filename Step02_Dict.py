
#회원 1명의 데이터
mem1={"num":1, "name":"kimgura", "isMan":True}
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

#dict 안 내용 수정
mem1["num"] = 2
mem1["name"] = "YangJaehyeok"
mem1["isMan"] = False

#특정 key 값으로 저장된 내용 삭제
del mem1["isMan"]

#모든 값 삭제
mem1.clear()
#종료 후 비어있는 Dict

print("종료됩니다")
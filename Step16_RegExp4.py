# Step16_RegExp4.py
import re

if __name__=="__main__" :
    while True:
        # 임의의 문자열을 받는다
        user_id = input("아이디를 입력하시오(영문 대소문자, 숫자만 가능): ")

        # 입력한 문자열을 검증하여 조건에 맞으면 "가입되었습니다" 조건에 맞지 않으면 "사용할 수 없는 ID입니다"를 출력하는 프로그래밍
        if re.search("^[a-zA-Z0-9]+$", user_id):
            print("가입되었습니다")
        else:
            print("사용할 수 없는 ID입니다")
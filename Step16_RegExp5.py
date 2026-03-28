# Step16_RegExp5.py

import re

if __name__=="__main__" :
    while True:
        input_id = input("아이디 입력(영문자로 시작하고, 5~10글자 이내, 특수문자 X): ")

        # 위 조건에 맞으면 "가입되었습니다", 맞지 않으면 "사용할 수 없는 아이디입니다."가 출력되도록 해보세요.
        pattern = r"^[a-zA-Z][a-zA-Z0-9]{4,9}$"

        if re.search(pattern, input_id):
            print("가입되었습니다")
        else:
            print("사용할 수 없는 아이디입니다.")

        # + : 한 번 이상 반복 = {1,}
        # * : 0번 이상 반복 = {0,}
        # ? : 0번 또는 1번 = {0,1}

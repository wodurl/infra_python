# Step14_TryExcept.py

# main으로 실행(현재 파일에서 run했을 때, import는 X)했을 때 실행할 Code 블럭
if __name__=="__main__" :
  
  while True:
    try:
        # 문자열
        num1_str: str = input("젯수 입력 : ")
        num2_str: str = input("피젯수 입력 : ")

        num1: int = int(num1_str) # 형 변환
        num2: int = int(num2_str) # 동생 변환은 없나? 깔깔

        result = num2 / num1
        print(f"{num2}를 {num1}으로 나눈 결과값 : {result}") # 결과를 출력
    except ValueError as ve: # ve에는 에러 정보가 들어있다.
        print(ve)
        print('숫자 형식으로 입력해 주세요')
    except ZeroDivisionError as zde: # ve에는 에러 정보가 들어있다.
        print(zde)
        print('어떤 수를 0으로 나눌 순 없어요')

    # 어떤 중요한 마무리 작업을 합니다.
    print("중요한 마무리 작업을 합니다.")
# BinaryTest/gui02.py

# ui ToolKit 을 사용할수 있는 interface 객체 import 하기 
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # 좌우 공백 제거 strip()
    # 빈 값일 경우 안내 문구 표시
    if not input_value: # 어떤 값도 입력받지 못하면
        return  # 함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수 종료)

    try:
        # 입력한 문자열을 정수로 변환
        num = int(input_value)
        # 만일 입력한 수가 0 <= num <= 255가 아니라면 경고 알림 띄우기
        if not (0 <= num <= 255): # Python에선 and 조건 없이 범위 비교 연산 가능
            messagebox.showerror("에러","0~255 사이의 숫자를 입력하세요.")
            return

        # 2진수 형태의 문자열로 변경해서
        binary_result = f"{num:08b}"
        # 출력하기
        result_label.config(text=binary_result, fg='blue')
    except Exception as e:
        result_label.config(text="숫자만 입력 가능합니다.", fg="red")
   

if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정 
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="10 진수를 2진수로 변환")
    # pady => padding y => y축 padding => 위아래 padding
    label.pack(pady=20)

    # 입력창 
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    # 결과 값을 출력할 Label
    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)

    # 창이 닫힐때 까지 무한 대기
    root.mainloop()
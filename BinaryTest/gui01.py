# gui01.py

# ui Toolkit을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk

# 버튼
def clicked():
    print("버튼을 클릭했네여!")
    # Entry에 입력한 문자열 받아오기
    name = name_entry.get()
    # label text 수정하기
    label2.config(text=f"입력한 이름: {name}")


if __name__=="__main__" :
    # root 창 생성. root는 Tk 타입 객체
    root = tk.Tk()
    # 제목 설정
    root.title("my App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블 출력
    label = tk.Label(root, text="안녕하세요! Python GUI입니다")
    # pady -> padding y -> y축 위아래 padding 설정
    label.pack(pady=20)

    # 입력창
    name_entry = tk.Entry(root, font=("Arial", 12), width=30)
    name_entry.pack(pady=5)
    name_entry.focus() # 포커스 주기

    btn = tk.Button(root, text="전송", command=clicked, width=10, bg='lightgray') 
    # 함수를 만들어 Command의 인자를 준다면, 버튼이 눌릴 때마다 함수가 호출
    btn.pack(pady=15)

    label2 = tk.Label(root,text="결과...")
    label2.pack(pady=20)

    # 창이 닫힐 때까지 무한 대기
    root.mainloop()
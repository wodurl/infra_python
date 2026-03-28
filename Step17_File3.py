# Step17_File3.py

import os

if __name__=="__main__" :
    # 읽어올 text 문서의 경로 구성하기
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "r", encoding='utf-8') as f:
        # 문자열을 한 줄씩 읽어서 콘솔에 출력
        # 한 칸씩 떨어진 이유? my_letter.txt에 한 줄의 마지막에 \n이 박혀있다고 생각하면 됨.
        # 그리고 print() 함수 자체도 \n을 출력하기 때문에, 두 번의 \n이 출력된다고 생각하면 됨.
        print(f.readline()) # f.readline()에 이미 개행기호가 포함되어 있음.
        print(f.readline())
        print(f.readline())
        print(f.readline().strip()) # 공백이나 개행기호를 없애고 싶으면 .strip()까지 호출한다.
        print(f.readline().strip())
        print(f.readline().strip())
        
    print("반복문으로 처리---------------------------------------")

    with open(letter_path, 'r', encoding='utf-8') as f:
        for line in f: # 파일 객체의 line을 순회
            print(line.strip())
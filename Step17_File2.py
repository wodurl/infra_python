# Step17_File.py

import os

if __name__=="__main__" :
    # 새로운 파일을 만들어서 문자열을 파일에 출력하기

    letter_path=os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "w", encoding='utf=8') as f:
        f.write("To my Freind")
        f.write("\nHello")
        f.write("\nI love you")

    with open(letter_path, "a", encoding='utf-8') as f:
        for i in range(14):
            f.write("북치기")
            f.write("박치기")
        
    print("my_letter.txt 파일 생성 및 쓰기 완료")
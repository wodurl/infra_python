# Step17_File.py

import os
# 객체 = 기능 + 저장소

if __name__=="__main__" :
    # 현재 작업 폴더의 경로 os.getcwd()
    # cwd : Current Working Directory
    print(os.getcwd())
    # 파일 구분자 os.sep (window는 역슬래시, linux는 슬래시)
    print(os.sep)
    r'''
        앞에 r을 붙이면 주석을 훨씬 쉽게 할 수 있음 ㅅㄱ
        현재 memo.txt 파일은 C:\playground\python_basic\memo.txt
    '''

    # 읽어올 파일의 절대경로 구성
    # os.path.join()을 이용하면 window에선 \로 조합하고 linux에선 /로 조합한다
    path:str = os.path.join(os.getcwd(),"memo.txt")
    print(path)

    with open(path, "r", encoding="utf-8") as f:
        # 파일에서 문자열 읽기
        result = f.read()
        print("=== memo.txt 파일 내용 ===")
        print(result)
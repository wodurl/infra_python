# Step13_example2.py

'''
    html/index.html 외부에 있는 template 파일을 읽어와서
    data를 연결해서 원하는 문자열을 얻어내서
    콘솔 창에 출력하는 예제(나중에는 콘솔창이 아니고 클라이언트의 웹 브라우저에 출력하게 된다.)

'''

from jinja2 import Environment, FileSystemLoader, Template

# 템플릿 파일이 위치한 폴더 설정
file_loader = FileSystemLoader("html")

# 환경 객체(외부 파일에서 읽어올 환경 설정을 한다)
env = Environment(loader=file_loader)

# 템플릿 파일 읽어오기
temp:str = env.get_template("index.html")

# 템플릿에 렌더링할 데이터 (실제로는 DB에서 읽어오게 된다)
notice_data = {
    "title": "오늘의 공지사항",
    'notice': ["드디어 불금입니다", "이러쿵..", '저러쿵..']
}

# 렌더링하기
result:str = temp.render(notice_data)

# 출력하기
print(result)
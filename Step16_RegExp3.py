# Step16_RegExp3.py

logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# logs 에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력해 보세요.

import re

for log in logs:
    if re.match(r'\[ERROR\]|\[WARN\]', log) is not None:
        print(log)
    # if re.match(r'\[WARN\]', log) is not None:
    #     print(log)
# print(logs_error)
# print(logs_warn)

# 첫 글자가 W or A or R or N인지를 검증할 수 있는 정규 표현식
pattern1 =r"^[WARN]"
# [WARN]으로 시작하는지 검증할 수 있는 정규 표현식
pattern2 =r"^\[WARN\]"
# [ERROR]으로 시작하는지 검증할 수 있는 정규 표현식
pattern3 =r"^\[ERROR\]"
# [WARN] or [ERROR]으로 시작하는지 검증할 수 있는 정규 표현식
pattern4 =r"^(WARN|ERROR)"
# [WARN] or [ERROR]으로 시작하는지 검증할 수 있는 정규 표현식
pattern =r"^\[(WARN|ERROR)\]"

for tmp in logs:
    if re.search(pattern, tmp): print(tmp)
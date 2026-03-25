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
    if re.match(r'\[ERROR\]', log) is not None:
        logs_error = log
    if re.match(r'\[WARN\]', log) is not None:
        logs_warn = log

print(logs_error)
print(logs_warn)
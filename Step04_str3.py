info = '''
name: 양재혁
addr: 순천
food:
  - 초밥
  - 피자
isMan: true
body:
  weight: 75
  height: 174
'''

# yaml 문자열을 다룰 때는 외부 모듈을 pip로 설치하여 import를 해야 한다.

# 과제
# 검색 혹은 AI의 도움을 받아 info에 들어있는 문자열을 dict 타입으로 바꾸시요
# 그런 다음 dict에 들어있는 내용을 확인 후 다시 dict에 있는 내용을 이용하여 yaml 문자 형식으로 변환하시오.

# yaml -> dict
import yaml
yaml_data = yaml.safe_load(info)
print(yaml_data)
print(type(yaml_data))

# dict -> yaml
trans_yaml = yaml.dump(yaml_data, allow_unicode=True, sort_keys=False) # allow_unicode=True를 추가하며 인코딩 깨짐 문제를 해결
                                                                        # sort_keys=False를 추가하며 yaml 데이터의 순서 정렬
print(trans_yaml)
print(type(trans_yaml))
# Step11_class2.py

class Mycar:
  # 객체가 생성될 때 호출되는 생성자
  # self 에는 생성된 객체의 주소값이 들어 있다
  def __init__(self, name: str):
    print("생성자가 호출됨")
    print(self)
    # 객체 고유의 저장소에 전달된 값을 전달한다
    self.name = name

  def drive(self):
    print(f"{self.name} 달려요")

if __name__=="__main__" :
  c1: Mycar = Mycar("마티즈")
  c2: Mycar = Mycar("아반떼")
  c1.drive()
  c2.drive()
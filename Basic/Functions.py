class Person:
  def __init__(self, name, name2):
    self.name = name
    self.name2 = name2

  def say_hello(self):
    print("안녕하세요 저는 " + self.name + " 입니다.")

  def introduce(self):
    print("잘 부탁드립니다 " + self.name2 + "씨.")

Seong = Person("허윤성", "아무개")
Seong.say_hello()
Seong.introduce()

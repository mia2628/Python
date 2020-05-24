class Person:
  def __init__(self, name, grad, score, port, vol):
    self.name = name
    self.grad = grad
    self.score = score
    self.port = port
    self.vol = vol

  def say_hello(self):
    print("안녕하세요 저는 " + self.name + " 입니다.")

  def check_graduate(self):
    if self.score > "130":
      if self.port == "O":
        if self.vol > "150":
          print("졸업여부 : " + "True")
        else:
          print("졸업여부 : " + "False")
      else:("졸업여부 : " + "False")
    else:
      print("졸업여부 : " + "False")

  def school_grade(self):
    print("수강학점 : " + self.score + "점")

  def portfolio(self):
    print("포트폴리오 제출여부 : " + self.port)

  def volunteer(self):
    print("봉사시간 : " + self.vol)

Seong = Person("허윤성", "", "128", "O", " 150H")
Seong.say_hello()
Seong.check_graduate()
Seong.school_grade()
Seong.portfolio()
Seong.volunteer()

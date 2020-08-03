class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)

  def get_average(self):
    total_score = 0
    for grade in self.grades:
      total_score += grade.score
    return total_score / len(self.grades)


class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    if self.score >= self.minimum_passing:
      return "Congrats! {score} is a passing grade".format(score = self.score)
    else:
      return "{score} isn't high enough to pass. You needed {minimum_passing} to pass".format(score = self.score, minimum_passing = self.minimum_passing)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieters_maths_grade = Grade(100)
pieters_english_grade = Grade(50)
print(pieters_maths_grade.is_passing())
print(pieters_english_grade.is_passing())
pieter.add_grade(pieters_maths_grade)
pieter.add_grade(pieters_english_grade)
print(pieter.get_average())
class Classroom(object):

  def __init__(self, room_number="", students=[]):
    self.students = students
    self.room_number = room_number

  def get_JSON_dict(self):
    d = vars(self)
    student_list = []
    for student in self.students:
      student_list.append(vars(student))
    d['students'] = student_list
    return d



class Student(object):

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
    self.__dict__ = {"name":self.name, "grade":self.grade}



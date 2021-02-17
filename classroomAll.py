

class Person(object):

	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName =  lastName

	def fullName(self):
		print(self.firstName + " " + self.lastName)


class Student(Person):
	def  __init__(self, firstName, lastName, subject):
		super(Student, self).__init__(firstName, lastName)
		self.subject = subject

	def subject(self):
		return self.subject

	def fullNameSubject(self):
		return  "%s %s, %s" %(self.firstName, self.lastName, self.subject)

class Teacher(Person):
	def __init__(self, firstName, lastName, course):
		super(Teacher, self).__init__(firstName, lastName)
		self.course = course

	def course(self):
		return self.course

	def fullNameCourse(self):
		return "%s %s, %s" %(self.firstName, self.lastName, self.course)

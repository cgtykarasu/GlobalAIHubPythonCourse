__author__ = "Çağatay KARASU"
__course__ = "Introduction to Python Programming"


class Manager:
		def __init__(self, fName, lName):
				self.fName = fName
				self.lName = lName
				self.language = []
				self.age = 0

		def addLanguage(self):
				while True:
						newLanguage = input("What language(s) do you speak? (for quit type 'q' please) : ")
						if newLanguage == "q" or newLanguage == "Q":
								break
						else:
								newLanguage = newLanguage.title()
								self.language.append(newLanguage)

				self.language = list(dict.fromkeys(self.language))

				languagesStr = ' '.join([str(i) for i in self.language])

				print(self.fName, self.lName, "knows", languagesStr)

		def setAge(self):
				age = int(input("Write your age please : "))
				self.age = age
				print(self.fName, self.lName, "'s age is :", age)

		def managerInfo(self):
				# print("This company's manager is", self.fName, self.lName, "He/She is", self.age, "years old.")
				print('{}{} {}.{}{} {}'
							.format("This company's manager is ", self.fName, self.lName, " He/She is ", self.age, "years old."))

				print("He/She speaks : ", ' '.join([str(i) for i in self.language]))


class Employees(Manager):
		def __init__(self, fName, lName):
				super().__init__(fName, lName)

		def welcomeEmployee(self):
				print("Welcome to our company", self.fName, self.lName)


employee = Employees("Çağatay", "Karasu")
employee.welcomeEmployee()
employee.setAge()
employee.addLanguage()
print("# " + "=" * 78 + " #")
manager = Manager("Çağatay", "KARASU")
manager.setAge()
manager.addLanguage()
print("# " + "=" * 78 + " #")
manager.managerInfo()

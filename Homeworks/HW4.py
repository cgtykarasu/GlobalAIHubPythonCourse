__author__ = "Çağatay KARASU"
__course__ = "Introduction to Python Programming"


class Animals:
		def __init__(self, color, legs, age):
				self.color = color
				self.legs = legs
				self.age = age

				# print("This animal's color is",color,",has",legs,"legs and it is",age,"years old.")
				print('{}{},{}{}{}{}{}'
							.format("This animal's color is ", color, " has ", legs, " legs and it is ", age," years old."))


class Dogs(Animals):
		def __init__(self, color, legs, age, name, breed):
				super().__init__(color, legs, age)
				self.name = name
				self.breed = breed
				print("This dog's name is", name, "and it's breed is", breed)

		@staticmethod
		def make_sound():
				print("Woof Woof!")


class Cats(Animals):
		def __init__(self, color, legs, age, name, breed):
				super().__init__(color, legs, age)
				self.name = name
				self.breed = breed
				print("This cat's name is", name, "and it's breed is", breed)

		@staticmethod
		def make_sound():
				print("Meow!")


animal = Animals("yellow", 4, 10)
print("# " + "=" * 78 + " #")
dog = Dogs("black", 4, 7, "Çomar", "Kangal")
dog.make_sound()
print("# " + "=" * 78 + " #")
cat = Cats("white", 4, 5, "Minnoş", "Turkish Van")
cat.make_sound()

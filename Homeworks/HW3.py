__author__ = "Çağatay KARASU"
__course__ = "Introduction to Python Programming"


def find_prime():
		startPoint = 0
		stopPoint = 100
		primeNums = []

		for num in range(startPoint, stopPoint):
				if num > 1:
						for i in range(2, num):
								if (num % i) == 0:
										break
						else:
								primeNums.append(num)

		print(primeNums)


find_prime()

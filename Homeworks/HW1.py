import math

print ("\n>>>>>>>>>>          FIRST ANSWER          <<<<<<<<<<\n")
list01 = ["Çağatay", "KARASU", "Introduction to Python Programming Course", 2021]
list02 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
finalList01 = []
finalList02 = []

if len(list01) % 2 == 0:
		for i in list01[int(len(list01) / 2):int(len(list01))]:
				finalList01.append(i)

		for i in list01[0:int(len(list01) / 2)]:
				finalList01.append(i)

else:
		for i in list01[int(math.ceil(len(list01) / 2)):int(len(list01))]:
				finalList01.append(i)

		finalList01.append(list01[int(len(list01) / 2)])

		for i in list01[0:(int(len(list01) / 2))]:
				finalList01.append(i)

print("My first list before swapping : ", list01)
print("My first list after swapping : ", finalList01)

if len(list02) % 2 == 0:
		for i in list02[int(len(list02) / 2):int(len(list02))]:
				finalList02.append(i)

		for i in list02[0:int(len(list02) / 2)]:
				finalList02.append(i)

else:
		for i in list02[int(math.ceil(len(list02) / 2)):int(len(list02))]:
				finalList02.append(i)

		finalList02.append(list02[int(len(list02) / 2)])

		for i in list02[0:(int(len(list02) / 2))]:
				finalList02.append(i)

print("My second list before swapping : ", list02)
print("My second list after swapping : ", finalList02, "\n")

print (">>>>>>>>>>          SECOND ANSWER          <<<<<<<<<<\n")

n = int(input("Enter a positive integer value please : "))
evenNumbers = []
oddNumbers = []

while n <= 0:
		print("Your number is not positive integer value!")
		n = int(input("Enter a positive integer value please : "))

while n > 0:
		for i in range(0, n + 1):
				if (i % 2) == 0:
						evenNumbers.append(i)
				else:
						oddNumbers.append(i)
		break

print("Even numbers between 0 to", n, "are : ", evenNumbers)
print("Odd numbers between 0 to", n, "are : ", oddNumbers)



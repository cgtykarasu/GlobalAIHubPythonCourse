__author__ = "Çağatay KARASU"
__course__ = "Introduction to Python Programming"

username01 = "Çağatay"
password01 = "123asd"

getUsername01 = input("Write your username please : ")

if getUsername01 == username01:
		getPassword01 = input("Write your password please : ")
		print("Your username&password are correct. You are logging in...") \
				if getPassword01 == password01 \
				else print("Your password is not correct")
else:
		print("Username is not found!")

print("\n" + '>'*10 + ' '*10 + "EXTRA" + ' '*10 + '<'*10 + "\n")

user = {"username02": "Çağatay", "password02": "123asd"}

getUsername02 = input("Write your username please : ")

if getUsername02 in user.get("username02"):
		getPassword02 = input("Write your password please : ")
		print("Your username&password are correct. You are logging in...") \
				if getPassword02 == user.get("password02") \
				else print("Your password is not correct")
else:
		print("Username is not found!")

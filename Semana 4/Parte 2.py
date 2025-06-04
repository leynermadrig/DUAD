Name = input("What is your name? ")
Last_name = input("What is your last name? ")
Age = int (input("How old are you? "))

if (Age <= 3):
	print("You are a baby!")
elif (Age > 3) and (Age <= 10):
	print("You are a child")
elif (Age > 10) and (Age <= 12):
	print("You are a preteen!")
elif (Age > 12) and (Age <= 18):
	print("You are a teen!")
elif (Age > 18) and (Age <= 23):
	print("You are a young adult!")
elif (Age > 23) and (Age <= 64):
	print("You are a adult!")
elif (Age > 64 ):
	print("You are a senior citizen!")
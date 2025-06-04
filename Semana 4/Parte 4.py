Number1 = int (input("Please enter the first number "))
Number2 = int (input("Please enter the second number "))
Number3 = int (input("Please enter the third number "))

if (Number1 > Number2) and (Number1 > Number3):
	print(Number1)
elif (Number2 > Number3) and (Number2 > Number1):
	print(Number2)
elif (Number3 > Number2) and (Number3 > Number1):
	print(Number3)
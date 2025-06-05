import random
Random_number = random.randint(1, 10)
User_number = 0

while User_number!= Random_number:
    User_number = int (input ('Please enter a number '))

    if (User_number != Random_number):
        print ('You are wrong!')

print ('You are right!')
print (f'The secret number is {Random_number}!')

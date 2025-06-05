Name = input("Tell me your name ")
print (f'Your name is {Name}')

Number = int(input ("How old are? "))
print (f'{Name} is {Number} years old!')

Number2 = int(input ("Do you want to add age? "))
Number = Number + Number2
print (f'Your new age is {Number}')



Name_list = [
    'Student0',
    'Student1',
    'Student2',
    'Student3',
    'Student4',
    ]

ID_list = [
    int('0'),
    int('0'),
    int('0'),
    int('0'),
    int('0')
]

Grades = [
    int('0'),
    int('0'),
    int('0'),
    int('0'),
    int('0')
]



Name_list[0] = input ('What is your student name is? ')
print (f'Welcome {Name_list[0]}!')

ID_list[0] = int (input ('Please enter your student ID '))
print ('Your ID has been saved!')


Name_list[1] = input ('What is your student name is? ')
print (f'Welcome {Name_list[1]}!')

ID_list[1] = int (input ('Please enter your student ID '))
print ('Your ID has been saved!')


Name_list[2] = input ('What is your student name is? ')
print (f'Welcome {Name_list[2]}!')

ID_list[2] = int (input ('Please enter your student ID '))
print ('Your ID has been saved!')

Grades[0] = int (input (f'Please {Name_list[0]} enter your English grade '))
Grades[1] = int (input (f'Please {Name_list[1]} enter your English grade '))
Grades[2] = int (input (f'Please {Name_list[2]} enter your English grade '))


print ('The list of students and their IDs is ')
print (f'{Name_list[0]} ID {ID_list[0]} Grade {Grades[0]}')
print (f'{Name_list[1]} ID {ID_list[1]} Grade {Grades[1]}')
print (f'{Name_list[2]} ID {ID_list[2]} Grade {Grades[2]}')

Grades[0] = ID_list[0] + Grades[0]
Grades[1] = ID_list[1] + Grades[1]
Grades[2] = ID_list[2] + Grades[2]

print (f'Your ID student adding your English grade is {Grades[0]}!')
print (f'Your ID student adding your English grade is {Grades[1]}!')
print (f'Your ID student adding your English grade is {Grades[2]}!')


True_sums = (input ("Do you want to do some sums? "))

if (True_sums == "Yes"):
    Number3 = float (input ('Enter a number '))
    Number3 = Number3 + Grades[0]
    print(Number3)
    print('That is your number with the first student grade!')
    Number3 = 0
    Number3 = float (input ('Enter a second number '))
    Number4 = float (input ('Enter a third number '))
    Number4 = Number3 + Number4
    print (Number4)
else:
	print("We are done!")
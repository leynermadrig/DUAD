
Grades = [
    float('0'), #Variable
    float('0'), #aprovadas
    float('0'), #desaprovadas
    float('0'), #totales
]
Grades_pass = 0
Grades_reject = 0
Total_Grades = 0
Real_grades = 0
Counter = 0
Real_grades = int (input("How many grades will you enter? 10 grades is the limit "))

while (Real_grades!= Counter) and (Real_grades <= 10):
        
        Counter = (Counter + 1)
        Grades[0] = float (input (f'Please enter your grade number {Counter} '))
        
        if (Grades[0] >= 70): 
            Grades[1] = Grades[0] + Grades[1]
            Grades_pass = Grades_pass + 1
            Total_Grades = Total_Grades + 1 
            Grades [3] = Grades [3] + Grades [0]

        elif (Grades[0] < 70):
            Grades[2] = Grades[0] + Grades[2]
            Grades_reject = Grades_reject + 1
            Total_Grades = Total_Grades + 1 
            Grades [3] = Grades [3] + Grades [0]


if (Real_grades <= 10):

    Grades [3] = Grades [3] / Real_grades #Promedio total
    Grades [1] = Grades [1] / Grades_pass
    Grades [2] = Grades [2] / Grades_reject


    print (f'Your total average grades is {Grades[3]}%')



    if (Grades_pass == 0):
        print ('Bad news, your grades pass average is 0%')
    elif (Grades_pass > 0):
        print (f'Student, you have {Grades_pass} grades +70!')
        print (f'Your Pass average grades is {Grades[1]}%')

    if (Grades_reject == 0):
        print ('Good news, your grades reject average is 0!')
    elif (Grades_reject > 0):
        print (f'Student, you have {Grades_reject} grades -70!')
        print (f'Your Reject average grades is {Grades[2]}%')

else:
    print ('Thi program is only for 10 grades max!')



def selection_menu():
    while True:
        try:
            operation = int(input('\nWelcome back! Please select an operation:\n'
                            '1 - Enter a student or students\n'
                            '2 - View the students information\n'
                            '3 - View top 3 students grades\n'
                            '4 - View average of students\n'
                            '5 - Export data to CSV\n'
                            '6 - Import data from CSV file\n'
                            'Your choice: '))

            if 1 <= operation <= 6:              
                return operation
            else:
                print('The number entered is not valid! Please enter a number between 1 and 6.')
        except ValueError as error:
            print(f'You did not enter a valid number. Error: {error}')

def call_operation_execution(operation, students_dictionary):


    if operation == 1:
        from actions import operation_1_enter_student
        students_dictionary = operation_1_enter_student(students_dictionary)


    if operation == 2:
        from actions import operation_2_students_information
        operation_2_students_information(students_dictionary)

    if operation == 3:
        from actions import operation_3_top_grades
        operation_3_top_grades(students_dictionary)

    if operation == 4:
        from actions import operation_4_average_students
        operation_4_average_students(students_dictionary)

    if operation == 5:
        from data import operation_5_export_csv
        operation_5_export_csv(students_dictionary)
        

    if operation == 6:
        from data import operation_6_import_csv
        operation_6_import_csv(students_dictionary)

    return students_dictionary





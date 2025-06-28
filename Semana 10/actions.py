def operation_1_enter_student (students_dictionary):
    print ('Operation 1')

    while True:
        try:
            
            quantity = int(input('¿Who many students do you want to get into? '))

            if quantity > 0:
                break


        except ValueError as error:
            print(f'You did not enter a valid number. Error: {error}')



    for i in range(quantity):
        student = {}

        student = {
    'Name': input('Add a student name: '),
    'Section': input('Add a section: ')}

        # Función auxiliar para validar calificaciones
        def get_valid_grade(subject): #va a continuar pidiendo la nota hasta que sea la correcta
            while True:
                try:
                    grade = float(input(f'Add a {subject} qualification (0 to 100): '))
                    if 0 <= grade <= 100:
                        return grade
                    else:
                        print('Grade must be between 0 and 100.')
                except ValueError as error:
                    print(f'Invalid input. Error: {error}')

        # Recolectar todas las calificaciones validadas
        student['Spanish Calification'] = get_valid_grade('Spanish')
        student['English Calification'] = get_valid_grade('English')
        student['Social Studies Calification'] = get_valid_grade('Social Studies')
        student['Science Calification'] = get_valid_grade('Science')

        student['Average'] = (
    student['Spanish Calification'] +
    student['English Calification'] +
    student['Social Studies Calification'] +
    student['Science Calification']
) / 4
        students_dictionary.append(student)

    print ('We finish the registration!')


    return students_dictionary


def operation_2_students_information (students_dictionary):
    print ('Operation 2')

    for i, student in enumerate(students_dictionary, start=1): #Ayuda a acomodar el diccionario, mejora la visualizacion al usuario
        print(f"\nStudent {i}:")
        for key, value in student.items():
            print(f"{key}: {value}")

    if not students_dictionary:
        print ('\nThe students list is empty!')



def operation_3_top_grades (students_dictionary):
    print ('\n--- Operation 3: Top 3 Students by Average ---') 
    
    if not students_dictionary:
        print ('\nThe students list is empty! Cannot determine top 3.') 
        return # Salir si no hay estudiantes
    
    print ('This is the top 3 students by average grade!')
    
    # Crea una COPIA de los diccionarios si los vas a modificar para la presentación,solo extrae la información necesaria.


    students_with_average = []
    for s in students_dictionary:
        if 'Average' in s:
            students_with_average.append(s)
        else:
            # Puedes imprimir una advertencia o calcular el promedio si falta
            print(f"Warning: Student '{s.get('Name', 'Unknown')}' does not have an 'Average' key.")

    if not students_with_average:
        print("No students with calculated averages found to determine top 3.")
        return

    # Ordena la lista original (una copia es implícita al pasarla a sorted si no se modifica)
    # sorted devuelve una nueva lista ordenada
    top_3_sorted = sorted(students_with_average, key=lambda x: x['Average'], reverse=True)[:3]
    
    for i, student_data in enumerate(top_3_sorted, start=1):
        print(f"\nTop {i}:")
        # Accede a las claves que sí existen y que quieres mostrar
        print(f"  Name: {student_data.get('Name', 'N/A')}") # .get para evitar KeyError si la clave no existe
        print(f"  Section: {student_data.get('Section', 'N/A')}")
        print(f"  Average: {student_data.get('Average', 0):.2f}") # Formatea el promedio


def operation_4_average_students (students_dictionary):
    print ('\nOperation 4')
    counter = 0

    if not students_dictionary:
        print ('\nThe students list is empty!') 
    else:   
        students = students_dictionary 

        averages = [student['Average'] for student in students if 'Average' in student]

        if averages:
            averages_sum = sum(averages)
            counter = len(averages) # El contador es el número de promedios válidos

            total_average = averages_sum / counter
            print (f'\nThe total average of all the students is {total_average}!')
        else:
            print('\nNo students with valid averages found to calculate the overall average.')

        print ('\nThis is the average for each student:')

        for i, student in enumerate(students, start=1):
            print(f"\nStudent {i}:")
            print(f"Name: {student.get('Name', 'N/A')}")
            print(f"Section: {student.get('Section', 'N/A')}") 
            if 'Average' in student:
                print(f"Average: {student['Average']}")
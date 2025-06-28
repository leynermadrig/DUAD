def operation_5_export_csv (students_dictionary):

    print ('Operation 5')
    import csv

    student_headers = ( 
    'Name',
    'Section',
    'Spanish Calification',
    'English Calification',
    'Social Studies Calification',
    'Science Calification',    
    'Average',
    )
    with open('Semana 10/Student Control.csv', 'w', encoding='utf-8', newline='') as file: #file path es un ejemplo ficticio, tiene que ser la ruta de un archivo
        writer = csv.DictWriter(file, student_headers, delimiter='\t') #Con delimiter='\t' se hacen las tabulaciones
        writer.writeheader()
        writer.writerows(students_dictionary)

    print ('\nThe file was been export!')


import csv
import os # Para verificar si el archivo existe

# Define la ruta del archivo
CSV_FILE_PATH = 'Semana 10/Student Control.csv'

def operation_6_import_csv(students_dictionary):
    print('\nOperación 6: Importando datos desde CSV')

    # Verifica si el archivo existe antes de intentar abrirlo
    if not os.path.exists(CSV_FILE_PATH):
        print(f"Error: The file '{CSV_FILE_PATH}' do not exist.")
        return [] # Devuelve una lista vacía si no se encuentra el archivo

    imported_students_list = [] # Crea una nueva lista para almacenar los datos de los estudiantes importados

    try:

        with open(CSV_FILE_PATH, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t') # ¡Asegúrate de que este delimitador coincida con tu exportación!
            
            for row in reader:

                processed_row = {}
                for key, value in row.items():
                    # Intenta convertir los campos numéricos a flotante
                    if key in ['Spanish Calification', 'English Calification','Social Studies Calification', 'Science Calification', 'Average']:
                        try:
                            processed_row[key] = float(value)
                        except ValueError:
                            print(f"Advertencia: No se pudo convertir el valor '{value}' de '{key}' a número para el estudiante '{row.get('Name', 'Desconocido')}' durante la importación. Se mantendrá como texto.")
                            processed_row[key] = value # Mantiene como cadena si la conversión falla
                    else:
                        processed_row[key] = value # Mantiene otros campos como están

                students_dictionary.append(processed_row) # Agrega el diccionario de estudiante procesado a la lista
        
        print(f'Se importaron {len(students_dictionary)} estudiante(s) exitosamente desde "{CSV_FILE_PATH}".')
        return students_dictionary # Devuelve la lista de estudiantes importados
    
    except IOError as e:
        print(f"Error al leer el archivo CSV: {e}")
        return [] # Devuelve una lista vacía en caso de error de E/S
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la importación: {e}")
        return [] # Devuelve una lista vacía en cualquier otro error
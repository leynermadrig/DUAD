import csv


def write_csv_file(file_path, data, headers):


    with open(file_path, 'w', encoding='utf-8') as file: #file path es un ejemplo ficticio, tiene que ser la ruta de un archivo
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def games_dictionary ():

    games_dict = []

    try:
        
        quantity = int(input('¿Who many games do you whant to get into? '))

    except ValueError as error:
        print(f'You did not enter a valid number. Error: {error}')
        exit()



    for i in range(quantity):

        game = {
            'Name': input('Add a name game: '),
            'Gender': input('Add a gender game: '),
            'Development': input('Add a devep game: '),
            'Clasification ESRB': input('Add a ESRB clasification game: ')
        }
        games_dict.append(game)

    games_headers = ( 
    'Name',
    'Gender',
    'Development',
    'Clasification ESRB',
    )

    write_csv_file('Semana 8/games.csv', games_dict, games_headers)




games_dictionary()


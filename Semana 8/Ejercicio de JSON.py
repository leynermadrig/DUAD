import json


def read_json_file (file_path): #aqui se convierte se lee el json y se convierte en una lista de diccionarios de python
    with open(file_path, 'r', encoding='utf-8') as file:
        python_dictionary = json.load(file)

    return python_dictionary


def python_variable_modification(): #se agregan los valores del nuevo pokemon a una lista de python con todos los valores anteriores del archivo json

    python_pokemons = read_json_file ('Semana 8/Pokemons.json')

    try:
        pokemon = {

            
            'name': 
                {'english': input ('Please add a name for your Pokemon! ')},
            'type': [input ('What is the type of your Pokemon? ')],
            'base': {
                'HP': int(input ('Who much HP have you Pokemon ')),
                'Attack': int(input ('Who much Attack have you Pokemon ')),
                'Defense': int(input ('Who much Defense have you Pokemon ')),
                'Sp. Attack': int(input ('Who much Sp Attack have you Pokemon ')),
                'Sp. Defense': int(input ('Who much Sp Defense have you Pokemon ')),
                'Speed': int(input ('Who much Speed have you Pokemon '))
            }}
        
        python_pokemons.append(pokemon)
        write_json('Semana 8/Pokemons.json',python_pokemons)

        return python_pokemons
    

    except ValueError as error:
        print(f'You did not enter a valid number stat. Error: {error}')
        exit()


def write_json (file_path,data): #sobreescribe el archivo Pokemons de Json
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4) # ensure_ascii=False, indent=4 asegura el formato correcto para el archivo json


python_variable_modification()


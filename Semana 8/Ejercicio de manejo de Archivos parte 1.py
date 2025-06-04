def read_songs(file_enter,file_output):
    with open(file_enter, 'r', encoding='utf-8') as file: # Abre archivos unicamente para leerlos
        songs =  [line.strip() for line in file.readlines() if line.strip()] #line.strip() limpia cada línea (quita saltos de línea y espacios) // if line.strip() solo incluye líneas que no están vacías.
        songs = sorted (songs) #Ordena alfabeticamente toda una lista de variables de texto
        #print(songs)

    with open(file_output, 'w', encoding='utf-8') as file: #Abre archivos para crear o sobreescribir
        file.write("\n".join(songs))  # Convierte lista de valores string a un solo string, si los valores estan separados por "\n"
        print (file_output)

    with open(file_output, 'r', encoding='utf-8') as file:
        sorter_songs = file.read()
        print (sorter_songs)

read_songs('Semana 8/Songs.txt','Semana 8/Mac Miller Songs.txt') #Se puede usar cualquier archivo, solamente seleccionar uno de input que se quiere acomodar y otro para escribir el codigo acomodado
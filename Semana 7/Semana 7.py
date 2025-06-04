def suma (numero_1,numero_2,primer_intento,resultado,operacion):

    try:

        if primer_intento == False:
            resultado = (numero_1 + numero_2)
            primer_intento = True
            return resultado, primer_intento

        elif primer_intento and operacion == 1: # Se ejecuta despues del primer intento y despues de borrar (5)
            numero_2 = float(input('Por favor ingrese un numero '))
            resultado = resultado + numero_2
            primer_intento = True
            return resultado, primer_intento
        
    except ValueError as error:
        print(f'No ingreso un numero. Error: {error}')
        exit()
    


def resta (numero_1,numero_2,primer_intento,resultado):

    try:

        if primer_intento == False:
            resultado = (numero_1 - numero_2)
            primer_intento = True
            return resultado, primer_intento

        elif primer_intento:
            numero_2 = float(input('Por favor ingrese un numero '))
            resultado = resultado - numero_2
            primer_intento = True
            return resultado, primer_intento
        
    except ValueError as error:
        print(f'No ingreso un numero. Error: {error}')
        exit()


def multiplicacion (numero_1,numero_2,primer_intento,resultado):

    try:

        if primer_intento == False:
            resultado = (numero_1 * numero_2)
            primer_intento = True
            return resultado, primer_intento

        elif primer_intento:
            numero_2 = float(input('Por favor ingrese un numero '))
            resultado = resultado * numero_2
            primer_intento = True
            return resultado, primer_intento
        
    except ValueError as error:
        print(f'No ingreso un numero. Error: {error}')
        exit()



def division (numero_1,numero_2,primer_intento,resultado):

    try:

        if primer_intento == False:
            resultado = (numero_1 / numero_2)
            primer_intento = True
            return resultado, primer_intento

        elif primer_intento:
            numero_2 = float(input('Por favor ingrese un numero '))
            resultado = resultado / numero_2
            primer_intento = True
            return resultado, primer_intento
        
    except ValueError as error:
        print(f'No ingreso un numero. Error: {error}')
        exit()


def borrar (numero_1,numero_2,primer_intento,resultado):
    resultado = 0
    numero_1 = 0
    numero_2 = 0
    primer_intento = False
    return numero_1, numero_2, resultado, primer_intento



def operaciones ():
        
        
        resultado = 0
        primer_intento = False
        operacion = int(10)
        numero_1 = 0
        numero_2 = 0

        while True:


            try:
                operacion = int(input ('¿Que desea realizar, una Suma (1), una Resta (2), una Multiplicacion (3), o una Division (4)? Presione (5) para borrar '))
                if operacion > 5:
                    raise IndexError
                
            except IndexError as error:
                print(f'El numero que ingreso no es un numero valido.')

            except ValueError as error:
                print(f'La operacion a usar no existe en la lista. Error: {error}')
                exit()

            try:

                if primer_intento == False and operacion < 5:
                    numero_1 = float(input ('Por favor ingrese un numero (1) '))


            except IndexError as error:
                print(f'El primero numero que ingreso es no es valido. Error: {error}')

            except ValueError as error:
                print(f'No ingreso un numero. Error: {error}')
                exit()

            except NameError:
                exit()

            try:

                if primer_intento == False and operacion < 5:
                    numero_2 = float(input ('Por favor ingrese un numero (2) '))

            except IndexError as error:
                print(f'El segundo numero que ingreso es no es valido. Error: {error}')

            except ValueError as error:
                print(f'No ingreso un numero. Error: {error}')
                exit ()


            if operacion == 1:

                resultado, primer_intento = suma(numero_1, numero_2, primer_intento, resultado, operacion)
                print (f'El resultado es de {resultado}')
#                print (primer_intento) #solo lo uso para validar que primer intento funcione

            elif operacion == 2:
                resultado, primer_intento = resta(numero_1, numero_2, primer_intento, resultado)
                print (f'El resultado es de {resultado}')

            elif operacion == 3:
                resultado, primer_intento = multiplicacion(numero_1, numero_2, primer_intento, resultado)
                print (f'El resultado es de {resultado}')

            elif operacion == 4:
                resultado, primer_intento = division(numero_1, numero_2, primer_intento, resultado)
                print (f'El resultado es de {resultado}')

            elif operacion == 5:
                numero_1, numero_2, resultado, primer_intento = borrar(numero_1, numero_2, primer_intento, resultado)
                print (f'El resultado es de {resultado}')

operaciones()
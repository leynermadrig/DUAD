my_numbers = input ('Please enter a list of numbers ')
real_list = []
def my_list (my_numbers):
    
    list_one = list(map(int, my_numbers.split(',')))#convierte numeros enteros o strings en una lista, solo si esta separada por ','
    for number in list_one:
        counter = 0 
        if number > 1:
            
            for i in range (2,number): #Empieza la iteracion en 2 y termina justo antes del numero de la lista asignado en ese momento
                rest = number%i
                if rest == 0:
                    counter += 1
            if counter == 0:
                real_list.append(number)
    print (real_list)

my_list(my_numbers)



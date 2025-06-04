def plus (list_one):
    result = sum(list_one)
    return result

numbers = input ('Please enter a list of numbers ')
list_one = list(map(int, numbers.split(',')))# convierte numeros enteros o strings en una lista, solo si esta separada por ','

print (plus(list_one))
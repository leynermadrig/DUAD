my_text = input ('Please enter a list ')

def my_list (my_text):
    list_one = my_text.split('-') #convierte String en una lista, solo si esta separada por '-'
    list_one.sort(key=str.lower) #Acomoda en orden alfabetico sin importar mayusculas ni minusculas
    print (list_one)


my_list(my_text)

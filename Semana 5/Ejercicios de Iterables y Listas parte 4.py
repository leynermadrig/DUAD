List_one = [1, 
            2, 
            3, 
            4, 
            5, 
            6, 
            7, 
            8, 
            9]

index = 0
while index < len(List_one):
	
	if List_one [index] % 2 != 0:
		del List_one [index] #del para borrar numero - pop para borrar valores
	else:
		index += 1
 
print (List_one)
list_a = ['first_name', 'last_name', 'role']          
list_b = ['Leyner', 'Madrigal', 'Manufacturing_Technician']

Total = {

        list_a[0]:list_b[0],
        list_a[1]:list_b[1],
        list_a[2]:list_b[2]

}

My_list = ["David", "Alfredo", "Leyner", "role"]

for same in My_list : #Crea una variable "temporal" llamada same, hace una iteracion buscando un valor de My_list en Total
    if same in Total: 
        My_list.remove(same)

print (My_list)
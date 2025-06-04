List_one = [0, 
            0, 
            0, 
            0, 
            0, 
            0, 
            0, 
            0, 
            0, 
            0]

Top_number = 0
index = 0

for i in range (10):
    List_one [index] = int(input("Please enter a number "))
    
    if List_one[index] > Top_number:
        Top_number = List_one[index]
    index += 1


if index >= 9:
    print (List_one)
    print ("The bigger number is ", Top_number)
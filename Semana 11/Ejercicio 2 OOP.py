class Bus:
    max_passengers = 10
    passengers = []
    
    def add_passenger(self, person):

        if len(self.passengers) < self.max_passengers:
            self.passengers.append (person)

            print("The passengers are:", [p.name for p in self.passengers]) 
            #Hace print de unicamente los nombres de cada pasajero, esto porque dentro de la lista existe el parametro 'Person' que no es amigable con el usuario


    def rest_passenger(self):
        if len(self.passengers) > 0:
            valid_passenger = False

            print (f'Which passenger do you want to get down?' , [p.name for p in self.passengers])
            name_to_remove = input("Enter the name of the passenger to remove: ")

            for p in self.passengers: #Se usa un for para que busque nombre por nombre, es importante indicar que tiene que buscar en el parametro 'name'
                        
                        if p.name == name_to_remove:
                            
                            self.passengers.remove(p) #Cuando encuentra la coincidnecia la borra
                            print(f'{name_to_remove} has gotten down from the bus.')
                            valid_passenger = True

# Si no encontró el pasajero
            if not any(p.name == name_to_remove for p in self.passengers) and valid_passenger == False:       
                print(f'{name_to_remove} is not in the bus!')

        else:

            print ('The bus is empty!')           

class Person:
    def __init__(self,name):
        self.name = name


def main():
        
        bus_1 = Bus()
        
        while True:
            
            print ('Welcome to the bus, what do you want to do? Press 1 to add a passenger, Press 2 to get down a passenger, Press 3 to exit ')
            operation = input ()

            if operation == '1' and len(bus_1.passengers) <= 9:
                bus_1.add_passenger(Person(input('Please enter a passenger name ')))

            if operation == '1' and len(bus_1.passengers) >= 10:
                print ('The bus is full! ')

            if operation == '2': 
                bus_1.rest_passenger()

            if operation == '3':
                print ('The bus arrive!')
                exit()


main()



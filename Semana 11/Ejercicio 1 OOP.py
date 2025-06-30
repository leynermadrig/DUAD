class Circle():

    radius = 10


    def get_area (self,radius):
        PI = 3.1416 #Esto es opcional, pero me gusto
        area = radius * PI

        return area
    
my_circle = Circle()

print (my_circle.get_area(50))
print (my_circle.get_area(30))
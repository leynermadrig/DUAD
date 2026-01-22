class Circle():

    radius = 10


    def get_area (self):
        PI = 3.1416 #Esto es opcional, pero me gusto
        area = self.radius * PI

        return area
    

my_circle = Circle()
print (my_circle.get_area())
my_circle.radius = 5
print (my_circle.get_area())
#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_hello():
	print("Hello World!")
	print("Mi primera funcion")
	print_hello_world()
	

def print_hello_world():
	print("Hello Guy!")
	print("Mi segunda funcion")
	

print_hello()
print_hello_world()
#1. Intente accesar a una variable definida dentro de una función desde afuera.
#2.  Intente accesar a una variable global desde una función y cambiar su valor.

def loser(Number_two):
    Number_one = int(input ('You lose, please enter a number again '))
    if Number_one > Number_two:
        print ('In this try, you almost lost')


def winner():
    print ('Congratulations, you are the winner!')

Number_one = int(input ('Please enter a number '))
Number_two = int(input ('Please enter a number '))


if Number_one > Number_two:
    loser(Number_two)

elif Number_one < Number_two:
    winner()

else:
    print('It\'s a tie!')


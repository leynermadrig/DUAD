def addition(num1, num2, first_attempt, result, operation):
    try:
        if not first_attempt:
            result = num1 + num2
            first_attempt = True
            return result, first_attempt

        elif first_attempt and operation == 1:
            num2 = float(input('Please enter a number: '))
            result += num2
            return result, first_attempt

    except ValueError as error:
        print(f'You did not enter a valid number. Error: {error}')
        exit()


def subtraction(num1, num2, first_attempt, result):
    try:
        if not first_attempt:
            result = num1 - num2
            first_attempt = True
            return result, first_attempt

        elif first_attempt:
            num2 = float(input('Please enter a number: '))
            result -= num2
            return result, first_attempt

    except ValueError as error:
        print(f'You did not enter a valid number. Error: {error}')
        exit()


def multiplication(num1, num2, first_attempt, result):
    try:
        if not first_attempt:
            result = num1 * num2
            first_attempt = True
            return result, first_attempt

        elif first_attempt:
            num2 = float(input('Please enter a number: '))
            result *= num2
            return result, first_attempt

    except ValueError as error:
        print(f'You did not enter a valid number. Error: {error}')
        exit()


def division(num1, num2, first_attempt, result):
    try:
        if not first_attempt:
            result = num1 / num2
            first_attempt = True
            return result, first_attempt

        elif first_attempt:
            num2 = float(input('Please enter a number: '))
            result /= num2
            return result, first_attempt

    except ValueError as error:
        print(f'You did not enter a valid number. Error: {error}')
        exit()


def clear(num1, num2, first_attempt, result):
    result = 0
    num1 = 0
    num2 = 0
    first_attempt = False
    return num1, num2, result, first_attempt


def operations():
    result = 0
    first_attempt = False
    operation = int(10)
    num1 = 0
    num2 = 0

    while True:
        try:
            operation = int(input('What would you like to do? Addition (1), Subtraction (2), Multiplication (3), Division (4)? Press (5) to clear. '))
            if operation > 5:
                raise IndexError

        except IndexError:
            print('The number you entered is not valid.')

        except ValueError as error:
            print(f'The operation does not exist in the list. Error: {error}')
            exit()

        try:
            if not first_attempt and operation < 5:
                num1 = float(input('Please enter number (1): '))

        except IndexError as error:
            print(f'The first number you entered is not valid. Error: {error}')

        except ValueError as error:
            print(f'You did not enter a number. Error: {error}')
            exit()

        except NameError:
            exit()

        try:
            if not first_attempt and operation < 5:
                num2 = float(input('Please enter number (2): '))

        except IndexError as error:
            print(f'The second number you entered is not valid. Error: {error}')

        except ValueError as error:
            print(f'You did not enter a number. Error: {error}')
            exit()

        if operation == 1:
            result, first_attempt = addition(num1, num2, first_attempt, result, operation)
            print(f'The result is {result}')

        elif operation == 2:
            result, first_attempt = subtraction(num1, num2, first_attempt, result)
            print(f'The result is {result}')

        elif operation == 3:
            result, first_attempt = multiplication(num1, num2, first_attempt, result)
            print(f'The result is {result}')

        elif operation == 4:
            result, first_attempt = division(num1, num2, first_attempt, result)
            print(f'The result is {result}')

        elif operation == 5:
            num1, num2, result, first_attempt = clear(num1, num2, first_attempt, result)
            print(f'The result is {result}')


operations()

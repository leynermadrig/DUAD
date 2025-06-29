from menu import selection_menu, call_operation_execution


def main ():
    students_dictionary = []

    while True:
        operation = selection_menu()
        students_dictionary = call_operation_execution(operation,students_dictionary)


if __name__ == "__main__":
    main()

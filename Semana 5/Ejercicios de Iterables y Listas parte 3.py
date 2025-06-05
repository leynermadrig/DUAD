name_list = [
    'Value 0',
    'Value 1',
    'Value 2',
    'Value 3',
    'Value 4',
    ]


last_number = name_list.pop(-1)
first_number = name_list.pop(0)


name_list.append (first_number)
name_list.insert (0,last_number)

print (name_list)

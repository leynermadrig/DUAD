my_text = input ('Please enter a text ')

def upper_lower (my_text):
    counter = 0
    upper = 0
    lower = 0
    for i in my_text:
        if my_text[counter].isupper():
            upper += 1
            counter += 1
        elif my_text[counter].islower():
            lower += 1
            counter += 1
        else:
            counter += 1    


    print(f'There is {upper} upper cases and {lower} lower cases')

upper_lower(my_text)

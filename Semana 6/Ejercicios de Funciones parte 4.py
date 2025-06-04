def reverse(my_text):
    reversed_text = ''
    for i in range(len(my_text) - 1, -1, -1):
        reversed_text += my_text[i]
    return reversed_text

my_text = input ('Please enter a text ')
print(reverse(my_text))
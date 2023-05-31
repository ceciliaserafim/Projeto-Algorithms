def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        central = array[0]
        small = [element for element in array[1:] if element <= central]
        big = [element for element in array[1:] if element > central]
        return quick_sort(small) + [central] + quick_sort(big)


def is_anagram(first_string, second_string):
    # converte as strings em lista letras, colocam em ordem e case insensitive
    letters_first_string = quick_sort(list(first_string.lower()))
    letters_second_string = quick_sort(list(second_string.lower()))
    # as listas de letras voltam a ser palavras
    first_string = ''.join(letters_first_string)
    second_string = ''.join(letters_second_string)

    if first_string == '' or second_string == '':
        return (first_string, second_string, False)

    if first_string == second_string:
        return (first_string, second_string, True)
    else:
        print("oi")
        return (first_string, second_string, False)


is_anagram("pedra", "perda")

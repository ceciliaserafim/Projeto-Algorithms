def is_anagram(first_string, second_string):
    # converte as strings em lista de letras, as embaralham e case insensitive
    letters_first_string = sorted(list(first_string).lower())
    letters_second_string = sorted(list(second_string).lower())
    # as listas de letras voltam a ser palavras
    first_string = ''.join(letters_first_string)
    second_string = ''.join(letters_second_string)

    if first_string or second_string == '':
        return False

    if first_string == second_string:
        return True
    else:
        return False

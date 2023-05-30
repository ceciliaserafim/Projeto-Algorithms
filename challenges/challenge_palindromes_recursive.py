def is_palindrome_recursive(word, first_letter, last_letter):
    if word == '':
        return False
    if first_letter >= last_letter:
        return True
    if word[first_letter] == word[last_letter]:
        return is_palindrome_recursive(word, first_letter + 1, last_letter - 1)
    else:
        return False

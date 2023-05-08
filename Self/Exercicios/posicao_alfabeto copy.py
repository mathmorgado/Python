def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(str(alphabet.index(x) + 1) + ' ' for x in text.lower() if x in alphabet).strip()


print(alphabet_position("The sunset sets at twelve o' clock."))
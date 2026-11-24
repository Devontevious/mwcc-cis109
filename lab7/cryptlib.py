def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char.isupper() else 'abcdefghijklmnopqrstuvwxyz'

            position = alphabet.index(char)
            new_position = (position + shift) % 26

            result += alphabet[new_position]
        else:
            result += char

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)

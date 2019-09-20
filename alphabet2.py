# Test alphabet

def alphabet(stringy):
    return ' '.join([str((ord(letter.upper()) - 64)) for letter in stringy if ord(letter.upper()) > 64 and ord(letter.upper()) <= 90])

print(alphabet(input("enter string")))
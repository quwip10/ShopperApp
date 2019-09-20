# Test alphabet

def alphabet(stringy):
    new_string = ''

    for letter in stringy:
        if ord(letter.upper()) > 64 and ord(letter.upper()) <= 90:
            new_string = new_string + ' ' + str((ord(letter.upper()) - 64))

    return new_string

print(alphabet(input("Input a string: ")))


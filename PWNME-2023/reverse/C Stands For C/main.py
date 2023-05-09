def caesar_cipher(message, shift):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            ascii_code = ord(char) + shift
            if char.isupper():
                if ascii_code > ord('Z'):
                    ascii_code -= 26
                elif ascii_code < ord('A'):
                    ascii_code += 26
            else:
                if ascii_code > ord('z'):
                    ascii_code -= 26
                elif ascii_code < ord('a'):
                    ascii_code += 26
            cipher_text += chr(ascii_code)
        else:
            cipher_text += char
    return cipher_text

for i in range(27):
    print(i,caesar_cipher("JQHGY{Qbs_x1x_S0o_nl13x_n0_f00E_Nb3l3}",i))
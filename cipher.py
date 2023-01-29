from library import *

def affinecipher(txt,a,b,mode):

    if a % 2 == 0 or a % 13 == 0:
        pass
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        count_txt = 0
        for char in txt:
            count_txt += 1
        
        if mode == 'encrypt':

            ord_char = [0 for i in range(count_txt)]

            for i in range(count_txt):
                x = 0
                for j in alphabet:
                    if j == txt[i]:
                        ord_char[i] = x
                        break
                    else:
                        x += 1
                ord_char[i] = (a * ord_char[i] + b) % length(alphabet)

            encrypted_txt = ''

            for i in range(count_txt):
                for j in range(length(alphabet)):
                    if ord_char[i] == j:
                        encrypted_txt += alphabet[j]

            return encrypted_txt

        elif mode == "decrypt":

            ord_char = [0 for i in range(count_txt)]

            for i in range(count_txt):
                x = 0
                for j in alphabet:
                    if j == txt[i]:
                        ord_char[i] = x
                        break
                    else:
                        x += 1
                ord_char[i] = (alphabet_multiplicative_inverse(a) * (ord_char[i] - b))% length(alphabet)

            decrypted_txt = ''

            for i in range(count_txt):
                for j in range(length(alphabet)):
                    if ord_char[i] == j:
                        decrypted_txt += alphabet[j]

            return decrypted_txt
                

def alphabet_multiplicative_inverse(key_a):
    for i in range(key_a):
        res = ((i * 26) + 1)/ key_a
        if int(res) == res:
            break

    return int(res)


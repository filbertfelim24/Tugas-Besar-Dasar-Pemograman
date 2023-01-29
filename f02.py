import cipher
from library import *

def register(data):
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    row_count = length(data)

    data_valid = True
    for row in data:
        if row[1] == username:
            data_valid = False

    if not data_valid :
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    else:
        username_valid = True
        for char in username:
            if ord(char) == 45 or ord(char) == 95 or (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
                continue
            else:
                username_valid = False

        password_valid = True
        for char in password:
            if 97 <= ord(char) <= 122:
                continue
            else:
                password_valid = False
        
        if not username_valid and not password_valid:
            print("Username dan password tidak valid, ulangi!")
        elif not username_valid:
            print("Username tidak valid, ulangi!")
        elif not password_valid:
            print("Password tidak valid, ulangi!")
        else:
            print(f"Username {username} telah berhasil register ke dalam \"Binomo\".")
            encrypted_pass = cipher.affinecipher(password,7,13,"encrypt")
            data += [[str(row_count+1),username,nama,encrypted_pass,"User",'0']]



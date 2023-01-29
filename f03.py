import cipher

def login(data):
    login_username = input("Masukan username: ")
    login_pass = input("Masukan password: ")
    encrypted_login_pass = cipher.affinecipher(login_pass,7,13,"encrypt")
    
    valid = False
    for row in data:
        if row[1] == login_username:
            if row[3] == encrypted_login_pass:
                user_id = row[0]
                username = row[1]
                role = row[4]
                valid = True
                break
            else:
                continue
        else:
            continue
    
    if not valid:
        print("Password atau username salah atau tidak ditemukan.")
        role = None
        username = None
        user_id = None
        return valid, role, username, user_id
    else:
        print(f"Halo {username}! Selamat datang di \"Binomo\".")
        return valid, role, username, user_id

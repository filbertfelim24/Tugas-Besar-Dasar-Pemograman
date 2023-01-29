from library import *
# F11 - Search Game at Store

# KAMUS LOKAL
# GameExists = Bool (Bernilai True apabila masukan pengguna terdapat di dataa.csv, dan False apabila tidak ditemukan.)
# search_game_at_store = Function based on 5 inputs: id, name, price, category, and year
# cari 
# id = string (Game ke-n, pada fungsi menempati kedudukan "id")
# nama = string (Nama game, pada fungsi menempati kedudukan "name")
# harga = string (Harga game, pada fungsi menempati kedudukan "price")
# jenis = string (Kategori game, pada fungsi menempati kedudukan "category")
# tahun = string (Tahun rilis game, pada fungsi menempati kedudukan "year")

# ALGORITMA
def search_game_at_store(data):
    # Pemasukan nilai variabel sebagai starting point fungsi
    id = input("Masukkan ID Game: ")
    name = input("Masukkan Nama Game: ")
    price = input("Masukkan Harga Game: ")
    category = input("Masukkan Kategori Game: ")
    year = input("Masukkan Tahun Rilis Game: ")
    print("Daftar game pada toko yang memenuhi kriteria: ")
    
    # Variable GameExists dibuat sebagai bool
    GameExists = False
    
    # Arra
    cari = [0 for i in range(length(data))]
    isFiltered = True
    # Barisan game.csv di-loop untuk menemukan spesifikasi sesuai masukan pengguna
    for i in range(length(data)):
        if id == "":
            if name == "":
                if price == "":
                    if category == "":
                        if year == "":
                            store_game_list_print(data)
                            isFiltered = False
                            GameExists = True
                            break
                        else: # Ada nilai input year
                            if year == data[i][3]:
                                cari[i] = 1
                                GameExists = True

                    else: # Ada nilai input category
                        if year == "":
                            if category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True

                else: # Ada nilai input price
                    if category == "":
                        if year == "":
                            if price == price_alter_with_dot(data[i][4]):
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if price == price_alter_with_dot(data[i][4]) and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category
                        if year == "":
                            if price == price_alter_with_dot(data[i][4]) and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if price == price_alter_with_dot(data[i][4]) and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True

            else: # Ada nilai input name
                if price == "":
                    if category == "":
                        if year == "":
                            if name == data[i][1]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if name == data[i][1] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category:
                        if year == "":
                            if name == data[i][1] and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if name == data[i][1] and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                else: # Ada nilai input price
                    if category == "":
                        if year == "":
                            if name == data[i][1] and price == price_alter_with_dot(data[i][4]):
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if name == data[i][1] and price == price_alter_with_dot(data[i][4]) and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category
                        if year == "":
                            if name == data[i][1] and price == price_alter_with_dot(data[i][4]) and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if name == data[i][1] and price == price_alter_with_dot(data[i][4]) and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True

        else: # Ada nilai input id
            if name == "":
                if price == "":
                    if category == "":
                        if year == "":
                            if id == data[i][0]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada input nilai category
                        if year == "":
                            if id == data[i][0] and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada input nilai year
                            if id == data[i][0] and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                else: # Ada nilai input price
                    if category == "":
                        if year == "":
                            if id == data[i][0] and price == price_alter_with_dot(data[i][4]):
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and price == price_alter_with_dot(data[i][4]) and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category
                        if year == "":
                            if id == data[i][0] and price == price_alter_with_dot(data[i][4]) and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and price == price_alter_with_dot(data[i][4]) and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
            else: # Ada nilai input name
                if price == "":
                    if category == "":
                        if year == "":
                            if id == data[i][0] and name == data[i][1]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and name == data[i][1] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category
                        if year == "":
                            if id == data[i][0] and name == data[i][1] and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and name == data[i][1] and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                else: # Ada nilai input price
                    if category == "":
                        if year == "":
                            if id == data[i][0] and name == data[i][1] and price == price_alter_with_dot(data[i][4]):
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and name == data[i][1] and price == price_alter_with_dot(data[i][4]) and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
                    else: # Ada nilai input category
                        if year == "":
                            if id == data[i][0] and name == data[i][1] and price == price_alter_with_dot(data[i][4]) and category == data[i][2]:
                                cari[i] = 1
                                GameExists = True
                        else: # Ada nilai input year
                            if id == data[i][0] and name == data[i][1] and price == price_alter_with_dot(data[i][4]) and category == data[i][2] and year == data[i][3]:
                                cari[i] = 1
                                GameExists = True
    searched_game_data = []
    for i in range(length(cari)):
        if cari[i] > 0:
            searched_game_data += [data[i]]

    if isFiltered:
        if not GameExists:
            print("Game tidak ditemukan.")
        else:
            store_game_list_print(searched_game_data)

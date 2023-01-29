from library import *

def ubah_game(data):
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori : ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")

    for row in data:
        if row[0] == id_game:
            if nama_game == '':
                pass
            else:
                row[1] = nama_game
            if kategori == '':
                pass
            else:
                row[2] = kategori
            if tahun_rilis == '':
                pass
            else:
                row[3] = tahun_rilis
            if harga == '':
                pass
            else:
                row[4] = price_alter_with_dot(harga)
    

            

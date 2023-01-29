from library import *

def tambah_game(data):
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    if nama_game == '' or kategori == '' or tahun_rilis== '' or harga == '' or stok_awal == '':
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        tambah_game(data)
    else:
        id = split_id(data[length(data)-1][0])           
        game_id = "GAME" + id_plus_one(id)
        print(f"Selamat! Berhasil menambahkan game {nama_game}.")
        data += [[game_id,nama_game,kategori,tahun_rilis,harga,stok_awal]]
        



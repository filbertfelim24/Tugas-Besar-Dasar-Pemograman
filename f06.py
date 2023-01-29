from library import *

def ubah_stok(data):
    # Input Variabel
    id_game = input("Masukkan ID game: ")


    # Sebuah variabel indeks dibuat untuk menentukan letak ID game yang dimasukkan
    indeks = 0

    # Penetapan nilai variabel kondisi

    
    # Penetapan awal variabel ada_ID
    ada_ID = False

   
    for i in range(length(data)):
        if id_game == data[i][0]:
            indeks = i
            ada_ID = True
            break
    
    if not ada_ID :
        print("Tidak ada game dengan ID tersebut!")
    else: #Apabila ID ditemukan di game.csv 
        tambah_stok = int(input("Masukkan jumlah: "))
        kondisi = ""
        if tambah_stok > 0:
            kondisi = "ditambahkan"
        else:
            kondisi = "dikurangi"
        if int(tambah_stok) + int(data[indeks][5]) < 0:
            print(f'Stok game "{data[indeks][1]}" gagal dikurangi karena stok kurang. Stok sekarang: {data[indeks][5]} (< {tambah_stok * -1})')
        else: # Apabila nilai penjumlahan (atau pengurangan) lebih besar dari 0
            data[indeks][5] = tambah_stok + int(data[indeks][5])
            print(f"Stok game {data[indeks][1]} berhasil {kondisi}. Stok sekarang: {data[indeks][5]}.")

 




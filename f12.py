from library import *

# F12 - Top-Up Saldo

# KAMUS LOKAL
# username = string (user tujuan yang saldonya akan diubah)
# saldo = int (nilai uang yang akan ditambahkan maupun dikurangi)
# kondisi = string, initially empty (bergantung kepada nilai saldo)
# UserExists = bool (bernilai True apabila username terdapat pada user.csv, dan False apabila tidak)

# ALGORITMA
def topup(data):
    # Pemasukan input variabel sebagai starting point fungsi
    username = input("Masukan username: ")
    saldo = int(input("Masukan saldo: "))

    # Penetapan nilai variabel kondisi
    kondisi = ""
    if saldo > 0:
        kondisi = "bertambah"
    else:
        kondisi = "berkurang"
    
    # Penetapan awal variabel UserExists
    UserExists = False

    # user.csv di-loop untuk mencocokkan input dari username
    for i in range(length(data)):
        if username == data[i][1] and data[i][4] == "User":
            UserExists = True
            break
    
    # Keberlangsungan fungsi bergantung kepada nilai bool UserExists
    if not UserExists:
        print(f'Username "{username}" tidak ditemukan.')
    else: # Apabila UserExists bernilai True (username ditemukan di user.csv)
        if saldo + int(data[i][5]) < 0:
            print("Masukan tidak valid.")
        else: # Apabila nilai penjumlahan (atau pengurangan) lebih besar dari 0
            data[i][5] = str(saldo + int(data[i][5]))
            print(f"Top up berhasil. Saldo {data[i][2]} {kondisi} menjadi {data[i][5]}.")

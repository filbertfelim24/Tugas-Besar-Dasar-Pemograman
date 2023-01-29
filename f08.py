from library import *
from datetime import datetime

# F08 : Membeli Game
def buy_game(user_data,game_data,kepemilikan_data,riwayat_data,username):
    # Prosedur ini menggunakan parameter username lalu akan menerima input ID Game dari user
    # Lalu melakukan validasi apakah game sudah dimiliki, saldo user cukup, dan stok masih tersedia
    # Kemudian mengeluarkan output sesuai validasi tersebut

    # Input ID Game yang ingin dibeli oleh user
    id_game = input("Masukkan ID Game : ")

    # Data saldo dan ID user yang akan membeli game  
    indeks_data_user = 0
    for i in range(length(user_data)):
        if user_data[i][1] == username:
            indeks_data_user = i

    saldo_user = int(user_data[indeks_data_user][5])
    id_user = str(user_data[indeks_data_user][0])

    # Data harga, stok, dan nama game yang akan dibeli oleh user
    indeks_data_game = 0
    for i in range(length(game_data)):
        if game_data[i][0] == id_game:
            indeks_data_game = i

    harga_game = int(game_data[indeks_data_game][4])
    stok_game = int(game_data[indeks_data_game][5])
    nama_game = game_data[indeks_data_game][1]

    # Validasi 1 : Memastikan game sudah dimiliki user atau belum
    validasi_1 = True
    for i in range(length(kepemilikan_data)):
        if kepemilikan_data[i][0] == id_game and kepemilikan_data[i][1] == id_user:
            validasi_1 = False
    
    # Validasi 2 : Memastikan saldo user cukup atau tidak untuk membeli game
    validasi_2 = False
    if saldo_user >= harga_game:
        validasi_2 = True

    # Validasi 3 : Memastikan stok game yang ingin dibeli user masih tersedia atau tidak di toko
    validasi_3 = False
    if stok_game > 0:
        validasi_3 = True

    # Keluaran
    ## Kondisi 1 : Semua validasi terpenuhi
    if validasi_1 == True and validasi_2 == True and validasi_3 == True:
        print(f'Game "{nama_game}" berhasil dibeli!')
        # stok game di game.csv berubah
        for i in range(length(game_data)):
            if game_data[i][0] == id_game:
                game_data[i][5] = str(int(game_data[i][5])-1)
        # saldo user di user.csv berubah
        for i in range(length(user_data)):
            if user_data[i][1] == username:
                user_data[i][5] = str(int(user_data[i][5])-harga_game)
        # kepemilikan.csv berubah
        kepemilikan_data += [[id_game,id_user]]
        # riwayat.csv berubah
        riwayat_data += [[id_game,nama_game,str(harga_game),id_user,str(datetime.now().year)]]


    ## Kondisi 2 : Game sudah dimiliki oleh user
    elif validasi_1 == False:
        print(f'Anda sudah memiliki Game tersebut!')

    ## Kondisi 3 : Saldo user tidak cukup untuk membeli game
    elif validasi_2 == False:
        print(f'Saldo anda tidak cukup untuk membeli Game tersebut!')

    ## Kondisi 4 : Stok game yang ingin dibeli user tidak tersedia di toko
    elif validasi_3 == False:
        print(f'Stok Game tersebut sedang habis!')
    

from library import *

# F10 : Mencari game yang dimiliki dari ID dan tahun rilis
def search_my_game(user_data,game_data,kepemilikan_data,username):
    # Prosedur ini menggunakan parameter username
    # Lalu menerima input ID game serta tahun rilis game, namun bersifat tidak wajib
    # Kemudian mengeluarkan output daftar game pada inventory yang memenuhi kriteria input user

    # Validasi username yang masuk sudah benar dan terdaftar (sudah ada di file user.csv)

    # Input ID serta tahun rilis Game yang ingin dicari oleh user
    id_game = input("Masukkan ID Game : ")
    tahun_perilisan = input("Masukkan Tahun Rilis Game : ")

    # Data id user yang akan membeli game
    indeks_data_user = 0
    for i in range(length(user_data)):
        if user_data[i][1] == username:
            indeks_data_user = i

    id_user = str(user_data[indeks_data_user][0])

    # Data total game yang dimiliki user
    total_game_user = 0
    for i in range(length(kepemilikan_data)):
        if kepemilikan_data[i][1] == id_user:
            total_game_user += 1

    # Data game yang dimiliki user
    data_game_user = [["A" for j in range(5)] for i in range(total_game_user)]
    k = 0
    for i in range(length(kepemilikan_data)):
        if kepemilikan_data[i][1] == id_user:

            ## Data id game yang dimiliki user
            game_id = kepemilikan_data[i][0]

            ## Data nama, harga, kategori, dan tahun rilis game yang dimiliki user
            indeks_data_game = 0
            for j in range(length(game_data)):
                if game_data[j][0] == game_id:
                    indeks_data_game = j

            nama_game = game_data[indeks_data_game][1]
            harga_game = game_data[indeks_data_game][4]
            kategori = game_data[indeks_data_game][2]
            tahun_rilis = game_data[indeks_data_game][3]
            data_game_user[k] = [game_id,nama_game,harga_game,kategori,tahun_rilis]
            k += 1
    
    filtered_user_game = []
    # Kondisi 1 : User memasukkan semua input
    if id_game != "" and tahun_perilisan != "":    
        print()
        game_sesuai_kriteria = 0
        for i in range(total_game_user):
            if data_game_user[i][0] == id_game and data_game_user[i][4] == tahun_perilisan:
                filtered_user_game += [[data_game_user[i][0],data_game_user[i][1],data_game_user[i][2],data_game_user[i][3],data_game_user[i][4]]]
                game_sesuai_kriteria += 1
        if game_sesuai_kriteria == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            user_filtered_game_list_print(filtered_user_game)

    # Kondisi 2 : User hanya memasukkan input id game
    elif id_game != "" and tahun_perilisan == "":
        print()
        game_sesuai_kriteria = 0
        for i in range(total_game_user):
            if data_game_user[i][0] == id_game:
                filtered_user_game += [[data_game_user[i][0],data_game_user[i][1],data_game_user[i][2],data_game_user[i][3],data_game_user[i][4]]]
                game_sesuai_kriteria += 1
        if game_sesuai_kriteria == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            user_filtered_game_list_print(filtered_user_game)

    # Kondisi 3 : User hanya memasukkan input tahun perilisan game
    elif id_game == "" and tahun_perilisan != "":
        print()
        game_sesuai_kriteria = 0
        for i in range(total_game_user):
            if data_game_user[i][4] == tahun_perilisan:
                filtered_user_game += [[data_game_user[i][0],data_game_user[i][1],data_game_user[i][2],data_game_user[i][3],data_game_user[i][4]]]
                game_sesuai_kriteria += 1
        if game_sesuai_kriteria == 0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            user_filtered_game_list_print(filtered_user_game)

    # Kondisi 4 : User tidak memasukkan semua input
    elif id_game == "" and tahun_perilisan == "":
        print("Daftar game:")
        print()
        for i in range(total_game_user):
            filtered_user_game += [[data_game_user[i][0],data_game_user[i][1],data_game_user[i][2],data_game_user[i][3],data_game_user[i][4]]] 
        user_filtered_game_list_print(filtered_user_game)

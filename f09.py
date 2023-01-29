from library import *

# F09 : Melihat Game yang dimiliki
def list_game(user_data,game_data,kepemilikan_data,username):
    # Prosedur ini menggunakan parameter username
    # Lalu mengeluarkan output data game yang dimiliki oleh user
    # Apabila user belum memiliki game, maka akan ditampilkan pesan khusus

    indeks_data_user = 0
    for i in range(length(user_data)):
        if user_data[i][1] == username:
            indeks_data_user = i

    id_user = str(user_data[indeks_data_user][0])

    # Validasi : Memastikan apakah user sudah memiliki game atau belum
    flag = False
    for i in range(length(kepemilikan_data)):
        if kepemilikan_data[i][1] == id_user:
            flag = True
            break
    
    # Kondisi 1 : User tidak memiliki game
    if flag == False:
        print('Maaf, kamu belum membeli game. Ketik perintah "buy_game" untuk beli.')
    
    # Kondisi 2 : User sudah memiliki game
    elif flag == True:
        print("Daftar game:")
        user_game = []
        j = 1
        for i in range(length(kepemilikan_data)):
            if kepemilikan_data[i][1] == id_user:
                ## Data id game yang dimiliki user
                game_id = kepemilikan_data[i][0]

                ## Data nama, harga, kategori, dan tahun rilis game yang dimiliki user
                indeks_data_game = 0
                for i in range(length(game_data)):
                    if game_data[i][0] == game_id:
                        indeks_data_game = i

                nama_game = game_data[indeks_data_game][1]
                harga_game = game_data[indeks_data_game][4]
                kategori = game_data[indeks_data_game][2]
                tahun_rilis = game_data[indeks_data_game][3]
                user_game += [[game_id,nama_game,kategori,tahun_rilis,harga_game]]
                j += 1
        user_game_list_print(user_game)
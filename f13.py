from library import *

def riwayat(data,user_id):
    riwayat_user = []
    for i in range(length(data)):
        if data[i][3] == user_id:
            riwayat_user += [data[i]]
        
    if length(riwayat_user) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.")
    else:
        print("Daftar game: ")
        riwayat_user_list_print(riwayat_user)

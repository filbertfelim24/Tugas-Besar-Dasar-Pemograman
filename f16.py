import os
from library import *

def save(data):
    folder = input('\nMasukkan nama folder penyimpanan : ')
    file = ['user.csv','game.csv','kepemilikan.csv','riwayat.csv']
    header = [['id','username','nama','password','role','saldo'], 
            ['id','nama','kategori','tahun_rilis','harga','stok'],
            ['game_id','user_id'],
            ['game_id','nama','harga','user_id','tahun_beli']]
            
    dir = os.path.dirname(__file__)
    folder_path = os.path.join(dir, folder)

    for i in range(length(data)):
        file_path = os.path.join(folder_path, file[i])

        not_exist = True
        for root_dir_path, sub_dirs, files in os.walk(dir):
            if root_dir_path == folder_path:
                not_exist = False
                break
        
        if not_exist:
            os.mkdir(folder_path)
        if i == 0:
            write_user(file_path, data[i])
        elif i == 1:
            write_game(file_path, data[i])
        elif i == 2:
            write_kepemilikan(file_path, data[i])
        else:
            write_riwayat(file_path, data[i])

    animation(0.1)
    print('\nData telah disave!')
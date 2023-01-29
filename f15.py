import os
from library import *

def load(folder):
    dir = os.path.dirname(__file__)
    folder_path = os.path.join(dir, folder)
    file = ['user.csv','game.csv','kepemilikan.csv','riwayat.csv']

    not_exist = True
    for root_dir_path, sub_dirs, files in os.walk(dir):
        if root_dir_path == folder_path:
            not_exist = False
            break
    
    if not_exist:
        print(f'Folder {folder} tidak ditemukan.')
        user_data = None
        game_data = None
        kepemilikan_data = None
        riwayat_data = None
        return user_data, game_data, kepemilikan_data,riwayat_data
    else:
        for i in range(length(file)):
            file_path = os.path.join(folder_path, file[i])
            if i == 0:
                user_data = open_csv(file_path, 6)
            elif i == 1:
                game_data = open_csv(file_path, 6)
            elif i == 2:
                kepemilikan_data = open_csv(file_path, 2)
            else:
                riwayat_data = open_csv(file_path, 5)
        animation(0.5)
        print("\nSelamat datang di antarmuka \"Binomo\"")
        return user_data, game_data, kepemilikan_data,riwayat_data
from f02 import *
from f03 import *
from f04 import *
from f05 import *
from f06 import *
from f07 import *
from f08 import *
from f09 import *
from f10 import *
from f11 import *
from f12 import *
from f13 import *
from f14 import *
from f15 import *
from f16 import *
from f17 import *
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=str, nargs="?",default="")
    args = parser.parse_args()
    if args.folder == '':
        print("Tidak ada nama folder yang diberikan!")
        exit()
    else:
        user_data, game_data, kepemilikan_data,riwayat_data = load(args.folder)
        if user_data != None:           
            time.sleep(0.5)
            user_data = pricealter(user_data,5)
            game_data = pricealter(game_data,4)
            riwayat_data = pricealter(riwayat_data,2)
            data = [user_data, game_data, kepemilikan_data,riwayat_data]
            message = "Ketik perintah kamu atau \'help\' untuk melihat daftar perintah yang bisa dijalankan ^_^ "
            print(message)
            logged = False
            role = "Not logged"
            while not logged:
                print()
                command = input(">>> ")
                if command == "help":
                    # aman
                    help(role)
                elif command == "login":
                    # aman
                    logged, role, username, user_id = login(user_data)
                elif command == "exit":
                    # aman
                    exit()
                else:
                    if is_user_command(command) or is_admin_command(command):
                        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain \"login\"")
                    else:
                        print("Perintah tidak ada dalam sistem.")
            
            while logged:
                print()
                command = input(">>> ")
                if role == "Admin":
                    if command == "help":
                        # aman
                        help(role)
                    elif command == "register":
                        # aman
                        register(user_data)
                    elif command == "tambah_game":
                        # aman
                        tambah_game(game_data)
                    elif command == "ubah_game":
                        # aman
                        ubah_game(game_data)
                    elif command == "ubah_stok":
                        # aman
                        ubah_stok(game_data)
                    elif command == "list_game_toko":
                        # aman
                        list_game_toko(game_data)
                    elif command == "search_game_at_store":
                        # aman
                        search_game_at_store(game_data)
                    elif command == "topup":
                        # aman
                        topup(user_data)
                    elif command == "save":
                        # aman
                        save(data)
                    elif command == "exit":
                        # aman
                        keluar(data)
                    else:
                        if is_user_command(command):
                            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                        else:
                            print("Perintah tidak terdaftar dalam sistem.")
                else:
                    if command == "help":
                        # aman
                        help(role)
                    elif command == "list_game_toko":
                        # aman
                        list_game_toko(game_data)
                    elif command == "buy_game":
                        # aman
                        buy_game(user_data,game_data,kepemilikan_data,riwayat_data,username)
                    elif command == "list_game":
                        # aman
                        list_game(user_data,game_data,kepemilikan_data,username)
                    elif command == "search_my_game":
                        # aman
                        search_my_game(user_data,game_data,kepemilikan_data,username)
                    elif command == "search_game_at_store":
                        # aman
                        search_game_at_store(game_data)
                    elif command == "riwayat":
                        riwayat(riwayat_data,user_id)
                    elif command == "save":
                        # aman
                        save(data)
                    elif command == "exit":
                        # aman
                        keluar(data)
                    else:
                        if is_admin_command(command):
                            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                        else:
                            print("Perintah tidak terdaftar dalam sistem.")
        else:
            exit()



    



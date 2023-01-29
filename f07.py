from library import *

# F07 : List Game berdasarkan ID, Harga, atau Tahun Rilis
# FUNGSI UTAMA
def list_game_toko(data):
    # Fungsi diawali dengan masukan jenis sorting dari pengguna
    sort = input("Skema sorting: ")
    # boolean untuk mengecek input valid atau tidak untuk keperluan looping
    valid = True
    
    # Looping untuk menghasilkan output urutan data game.csv berdasarkan parameter tertentu
    if sort == "":
         # Sort berdasarkan Game ID, tinggal display datanya secara full aja
        for i in range(length(data) - 1):
                for j in range(0,length(data) - i - 1):
                    if int(split_id(data[j][0])) > int(split_id(data[j + 1][0])):
                            data[j], data[j + 1] = data[j + 1], data[j] 
        store_game_list_print(data)
    else: # Ada masukan input pada variabel sort
        for i in range(length(data) - 1):
            for j in range(0,length(data) - i - 1):
                if sort[:((length(sort)) - 1)] == "tahun":
                    if sort[(length(sort)) - 1] == "-":
                        if int(data[j][3]) < int(data[j + 1][3]):
                            data[j], data[j + 1] = data[j + 1], data[j]
                    elif sort[(length(sort)) - 1] == "+":
                        if int(data[j][3]) > int(data[j + 1][3]):
                            data[j], data[j + 1] = data[j + 1], data[j]
                    else: # elemen terakhir sort bukan - atau +
                        valid = False
                        print("Skema sorting tidak valid!")
                        break
                elif sort[:((length(sort)) - 1)] == "harga":
                    if sort[(length(sort)) - 1] == "-":
                        if int(data[j][4]) < int(data[j + 1][4]):
                            data[j], data[j + 1] = data[j + 1], data[j]
                    elif sort[(length(sort)) - 1] == "+":
                        if int(data[j][4]) > int(data[j + 1][4]):
                            data[j], data[j + 1] = data[j + 1], data[j]
                    else: # elemen terakhir sort bukan - atau +
                        valid = False
                        print("Skema sorting tidak valid!") 
                        break
                else: # Sort tidak mengandung unsur "harga" maupun "tahun"
                    valid = False
                    print("Skema sorting tidak valid!")
                    break
                if not valid:
                    break
            if not valid:
                break
        if valid:
            store_game_list_print(data)      
            # sort data game kembali berdasarkan game id
            for i in range(length(data) - 1):
                for j in range(0,length(data) - i - 1):
                    if int(split_id(data[j][0])) > int(split_id(data[j + 1][0])):
                            data[j], data[j + 1] = data[j + 1], data[j]
    



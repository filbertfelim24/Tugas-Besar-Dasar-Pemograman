# fungsi csv parser

def open_csv(file_dir,num_of_col):

    csv_data_and_header = [0 for line in open(file_dir)]
    row_count = 0
    for rows in csv_data_and_header:
        row_count += 1
    with open(file_dir) as file:   
        data_count = 0
        for line in file:
            data = ''
            row = [0 for col in range(num_of_col)]
            i = 0
            for char in line:
                if char == ',':
                    row[i] = data
                    data = ''
                    i += 1
                else:
                    if char == '\n':
                        break
                    data += char
            row[i] = data
            csv_data_and_header[data_count] = row
            data_count += 1

            csv_data = [0 for row in range(row_count-1)]

            for i in range(1,row_count):
                csv_data[i-1] = csv_data_and_header[i]

    return csv_data

# fungsi animasi loading
def animation(seconds):
    import sys
    import time
    animation = ["■■□□□□□□□□□□","■■■■□□□□□□□□", "■■■■■□□□□□□□", "■■■■■■□□□□□□", "■■■■■■■□□□□□", "■■■■■■■■□□□□", "■■■■■■■■■□□□", "■■■■■■■■■■□□", "■■■■■■■■■■■□", "■■■■■■■■■■■■"]
    for i in range (len(animation)):
        time.sleep(seconds)
        sys.stdout.write("\r"+ animation[i % len(animation)]+" "+str(i*10+10)+"%")
        sys.stdout.flush()
    time.sleep(seconds*5)

# fungsi len
def length(list):
    i = 0
    for char in list:
        i += 1
    return i
    
# fungsi convert list tanpa kolom harga ke string
def to_string_without_price(lst): 
    string = "" 
    i = 0
    for char in lst:
        string += char
        i += 1
        if length(lst) - i != 0:
            string += ','
    return string

# fungsi convert list dengan kolom harga ke string
def to_string_with_price(lst,col):
    string = ""
    i = 0
    for char in lst:
        if i == col-1:
            string += price_alter_with_dot(char)
        else:
            string += char
        i += 1
        if length(lst) - i != 0:
            string += ','
    return string

# fungsi menyusun string data user menjadi stack
def stacked_string_user(data):
    stacked = ''
    for i in range(length(data)):
        stacked += f'\n{to_string_with_price(data[i],6)}'
    return stacked

# fungsi menyusun string data game menjadi stack
def stacked_string_game(data):
    stacked = ''
    for i in range(length(data)):
        stacked += f'\n{to_string_with_price(data[i],5)}'
    return stacked

# fungsi menyusun string data kepemilikan menjadi stack
def stacked_string_kepemilikan(data):
    stacked = ''
    for i in range(length(data)):
        stacked += f'\n{to_string_without_price(data[i])}'
    return stacked

# fungsi menyusun string data riwayat menjadi stack
def stacked_string_riwayat(data):
    stacked = ''
    for i in range(length(data)):
        stacked += f'\n{to_string_with_price(data[i],3)}'
    return stacked
        
# fungsi write user.csv
def write_user(file_path, data):
    header = ['id','username','nama','password','role','saldo']
    with open(file_path, 'w') as f:
        f.write(to_string_without_price(header))
        f.write(stacked_string_user(data))

# fungsi write game.csv
def write_game(file_path,data):
    header = ['id','nama','kategori','tahun_rilis','harga','stok']
    with open(file_path, 'w') as f:
        f.write(to_string_without_price(header))
        f.write(stacked_string_game(data))

# fungsi write kepemilikan.csv
def write_kepemilikan(file_path,data):
    header = ['game_id','user_id']
    with open(file_path, 'w') as f:
        f.write(to_string_without_price(header))
        f.write(stacked_string_kepemilikan(data))

# fungsi write riwayat.csv
def write_riwayat(file_path, data):
    header = ['game_id','nama','harga','user_id','tahun_beli']
    with open(file_path, 'w') as f:
        f.write(to_string_without_price(header))
        f.write(stacked_string_riwayat(data))

# fungsi pricealter menghilangkan titik pada harga
def pricealter(data,col):
    for i in range(length(data)):
        price = ""
        for j in range(length(data[i][col])):
            if data[i][col][j] != ".":
                price = price + data[i][col][j]
        data[i][col] = price
    return data

def price_alter_with_dot(price):
    if int(price) < 1000:
        return str(price)
    else:
        thousands = length(price) // 3
        if length(price) % 3 == 0:
            thousands -= 1
        i = 0
        res = ""
        idx = -1
        while thousands != 0:
            res += price[idx]
            i += 1
            idx -= 1
            if i % 3 == 0:
                res += "."
                thousands -= 1
        start = price[:idx+1]
        end = res[::-1]
        return start+end
    
def is_user_command(command):
    user_command = ["login","list_game_toko","buy_game","list_game","search_my_game","search_game_at_store","riwayat","save","exit"]
    for com in user_command:
        if command == com:
            return True
    return False

def is_admin_command(command):
    admin_command = ["register","login","tambah_game","ubah_game","ubah_stok","list_game_toko","search_game_at_store","topup","save","exit"]
    for com in admin_command:
        if command == com:
            return True
    return False

def id_plus_one(x):
    if 0 < int(x) < 100:
        res = int(x) + 1
        return '0' + str(res)
    else:
        res = int(x) + 1
        return str(res)

def split_id(game_id):
    id = ''
    for char in game_id:
        try:
            value = int(char)
            id += str(value)
        except:
            continue
    return id

def store_game_list_print(data):
    name_max_length = 0
    category_max_length = 0
    price_max_length = 0
    year_max_length = 0
    id_max_length = 0
    for baris in data:
        if length(baris[0]) > id_max_length:
            id_max_length = length(baris[0])
        if length(baris[1]) > name_max_length:
            name_max_length = length(baris[1])
        if length(baris[2]) > category_max_length:
            category_max_length = length(baris[2])
        if length(baris[3]) > year_max_length:
            year_max_length = length(baris[3])
        if length(baris[4]) > price_max_length:
            price_max_length = length(baris[4])
    for i in range(length(data)):
        print(f"{i+1}.{print_spacing(length(str(i+1)),length(str(length(data))))} {data[i][0]}{print_spacing(length(data[i][0]),id_max_length)} | {data[i][1]}{print_spacing(length(data[i][1]),name_max_length)} | {data[i][4]}{print_spacing(length(data[i][4]),price_max_length)} | {data[i][2]}{print_spacing(length(data[i][2]),category_max_length)} | {data[i][3]}{print_spacing(length(data[i][3]),year_max_length)} | {data[i][5]}",end='\n')

def user_game_list_print(data):
    name_max_length = 0
    category_max_length = 0
    price_max_length = 0
    year_max_length = 0
    id_max_length = 0
    for baris in data:
        if length(baris[0]) > id_max_length:
            id_max_length = length(baris[0])
        if length(baris[1]) > name_max_length:
            name_max_length = length(baris[1])
        if length(baris[2]) > category_max_length:
            category_max_length = length(baris[2])
        if length(baris[3]) > year_max_length:
            year_max_length = length(baris[3])
        if length(price_alter_with_dot(baris[4])) > price_max_length:
            price_max_length = length(price_alter_with_dot(baris[4]))       
    for i in range(length(data)):
        print(f"{i+1}.{print_spacing(length(str(i+1)),length(str(length(data))))} {data[i][0]}{print_spacing(length(data[i][0]),id_max_length)} | {data[i][1]}{print_spacing(length(data[i][1]),name_max_length)} | {data[i][2]}{print_spacing(length(data[i][2]),category_max_length)} | {data[i][3]}{print_spacing(length(data[i][3]),year_max_length)} | {price_alter_with_dot(data[i][4])}{print_spacing(length(price_alter_with_dot(data[i][4])),price_max_length)}",end='\n')

def user_filtered_game_list_print(data):
    name_max_length = 0
    category_max_length = 0
    price_max_length = 0
    id_max_length = 0
    for baris in data:
        if length(baris[0]) > id_max_length:
            id_max_length = length(baris[0])
        if length(baris[1]) > name_max_length:
            name_max_length = length(baris[1])
        if length(price_alter_with_dot(baris[2])) > price_max_length:
            price_max_length = length(price_alter_with_dot(baris[2])) 
        if length(baris[3]) > category_max_length:
            category_max_length = length(baris[3])      
    for i in range(length(data)):
        print(f"{i+1}.{print_spacing(length(str(i+1)),length(str(length(data))))} {data[i][0]}{print_spacing(length(data[i][0]),id_max_length)} | {data[i][1]}{print_spacing(length(data[i][1]),name_max_length)} | {price_alter_with_dot(data[i][2])}{print_spacing(length(price_alter_with_dot(data[i][2])),price_max_length)} | {data[i][3]}{print_spacing(length(data[i][3]),category_max_length)} | {data[i][4]}",end='\n')

def riwayat_user_list_print(data):
    game_id_max_length = 0
    name_max_length = 0
    price_max_length = 0
    year_max_length = 0
    for baris in data:
        if length(baris[0]) > game_id_max_length:
            game_id_max_length = length(baris[0])
        if length(baris[1]) > name_max_length:
            name_max_length = length(baris[1])
        if length(price_alter_with_dot(baris[2])) > price_max_length:
            price_max_length = length(price_alter_with_dot(baris[2])) 
        if length(baris[4]) > year_max_length:
            year_max_length = length(baris[4])      
    for i in range(length(data)):
        print(f"{i+1}.{print_spacing(length(str(i+1)),length(str(length(data))))} {data[i][0]}{print_spacing(length(data[i][0]),game_id_max_length)} | {data[i][1]}{print_spacing(length(data[i][1]),name_max_length)} | {price_alter_with_dot(data[i][2])}{print_spacing(length(price_alter_with_dot(data[i][2])),price_max_length)} | {data[i][4]}{print_spacing(length(data[i][4]),price_max_length)}",end='\n')

# fungsi untuk keperluan print spacing di output
def print_spacing(input_length,max_length):
    return " " * (max_length-input_length)
def help(role):
    if role == 'Not logged':
        print('''
    Daftar command:
    1.  login -  Melakukan login ke dalam sistem
    2.  help  -  Menampilkan perintah yang dapat dijalankan oleh user
    3.  exit  -  Keluar dari aplikasi
    ''')
    
    elif role == "Admin":
            print('''
    Daftar command untuk role ADMIN:
    1.  help                    -  Menampilkan perintah yang bisa dijalankan oleh pengguna
    2.  register                -  Melakukan registrasi user baru
    3.  tambah_game             -  Menambah game yang dijual di toko
    4.  ubah_game               -  Mengubah mengubah informasi game yang dijual di toko'
    5.  ubah_stok               -  Mengubah stok game yang dijual di toko
    6.  list_game_toko          -  Melihat list game yang dijual di toko
    7.  search_game_at_store    -  Mencari game yang dijual di toko
    8.  topup                   -  Menambahkan saldo user
    9.  save                    -  Menyimpan perubahan data
    10. exit                    -  Keluar dari sistem
    ''')
    
    else:
            print('''
    Daftar command untuk role USER:
    1.  help                    -  Menampilkan perintah yang bisa dijalankan oleh pengguna
    2.  list_game_toko          -  Melihat list game yang dijual di toko
    3.  buy_game                -  Membeli game yang dijual di toko
    4.  list_game               -  Melihat game yang kamu miliki
    5.  search_my_game          -  Mencari game yang kamu miliki
    6.  search_game_at_store    -  Mencari game yang dijual di toko
    7.  riwayat                 -  Melihat riwayat pembelian game
    8.  save                    -  Menyimpan perubahan data
    9.  exit                    -  Keluar dari sistem
    ''')
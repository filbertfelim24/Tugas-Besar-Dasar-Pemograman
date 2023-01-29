from library import *
from prettytable.colortable import ColorTable, Themes
from prettytable import PrettyTable
help_not_logged = [[1,"login","Melakukan login ke dalam sistem"],
                    [2,"help","Menampilkan perintah yang bisa dijalankan oleh pengguna"],
                    [3,"exit","Keluar dari sistem"]]
help_user = [[1,"help","Menampilkan perintah yang bisa dijalankan oleh pengguna"],
                [2,"login","Melakukan login ke dalam sistem"],
                [3,"list_game_toko","Menampilkan daftar game yang dijual di toko BNMO"],
                [4,"buy_game","Membeli game yang dijual di toko"],
                [5,"list_game","Menampilkan daftar game yang dimiliki pengguna"],
                [6,"search_my_game","Menampilkan game yang dimiliki berdasarkan masukan pengguna"],
                [7,"search_game_at_store","Menampilkan game di toko berdasarkan masukan pengguna"],
                [8,"riwayat","Menampilkan riwayat pembelian game pengguna"],
                [9,"save","Menyimpan perubahan data ke dalam sistem"],
                ["exit","Keluar dari sistem"]]

help_admin = [[1,"help","Menampilkan perintah yang bisa dijalankan oleh pengguna"],
                [2,"register","Mendaftarkan pengguna baru ke dalam sistem"],
                [3,"login","Melakukan login ke dalam sistem"],
                [4,"tambah_game","Menambahkan daftar game yang ada di dalam toko"],
                [5,"ubah_game","Mengubah informasi game yang dijual di toko berdasarkan game ID"],
                [6,"ubah_stok","Mengubah banyak stok game yang dijual di toko berdasarkan game ID"],
                [7,"list_game_toko","Menampilkan daftar game yang dijual di toko BNMO"],                
                [8,"search_game_at_store","Menampilkan game di toko berdasarkan masukan pengguna"],
                [8,"topup","Menambah atau mengurangi saldo user"],
                [10,"save","Menyimpan perubahan data ke dalam sistem"],
                [11,"exit","Keluar dari sistem"]]





# game_data = open_csv("data/game.csv",6)
t = ColorTable(['No','Perintah','Deskripsi Perintah'],theme=Themes.OCEAN,)
t.add_rows(help_admin)
t.align['Deskripsi Perintah'] = 'l'
t.align['Perintah'] = 'l'
t.align['No'] = 'r'
# print(tabulate.tabulate(help_admin,headers=['No','Perintah','Deskripsi Perintah'],tablefmt="grid"))
print(t)
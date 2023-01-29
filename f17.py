from f16 import *

def keluar(data):
    penyimpanan = input('Apakah kamu mau melakukan penyimpanan file yang sudah diubah? (y/n) ').lower()

    if penyimpanan == 'y':
        save(data)
        print('\nTerima kasih telah bermain di BINOMO. Salam cuan!')
        exit()
    elif penyimpanan == 'n':
        print('\nData tidak disave!')
        print('Terima kasih telah bermain di BINOMO. Salam cuan!')
        exit()
    else:
        print('\nHarap memberi masukan yang sesuai!')
        keluar(data)
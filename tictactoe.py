# GAME BONUS : TICTACTOE

# KAMUS LOKAL
# ttt: matrix of characters, berfungsi sebagai tempat berlangsungnya game
# i : integer (initially hardcoded), digunakan untuk menentukan giliran pemain
# a , c : integer, sebagai letak baris masukan pemain
# b , d : integer, sebagai letak kolom masukan pemain
# isWin : boolean, bernilai True apabila ditemukan pemenang game
# Win : string, berisi pemenang game

# ALGORITMA
def tictactoe():
    # Pengantar awal game yang tampil pada layar
    print("""                                    Selamat datang pada game Tic-Tac-Toe! 
    Sebuah game klasik dimana kalian harus mengisi satu baris, satu kolom, atau satu diagonal secepat mungkin.
                            Terdapat 2 pemain, yaitu Pemain "X" dan Pemain "O".
                                    Selamat bermain, dan semoga beruntung!""")
    print("\n")

    # Penetapan nilai awal variabel isWin dan Win
    isWin = False
    Win = ""

    # Penetapan nilai awal variabel i sebagai penentu giliran
    i = 0

    # Penetapan matriks ttt dan pemanggilan matriks awal
    ttt = [["-" for k in range(3)] for l in range(3)]
    for l in range(3):
        for k in range(3):
            print(ttt[l][k], end = " ")
        print()
    print("\n")

    # Masukan matriks diloop sebelum penuh, yaitu hingga 9 masukan
    for i in range(9): # Apabila i ganjil, maka giliran jatuh ke pemain 1
        if (((i + 1) % 2) == 1):
            # Matriks menerima input dari pemain
            print(f"Giliran {int((i // 2) + 1)} Pemain X:")
            a = int(input("Lokasi mendatar pilihan: "))
            b = int(input("Lokasi vertikal pilihan: "))
            # Masukan input divalidasi
            while True:
                if (1 <= a <= 3 and 1 <= b <= 3) and ttt[a-1][b-1] == "-":
                    break
                elif (a < 1 or a > 3 or b < 1 or b > 3): # Masukan posisi tictactoe diluar jangkauan matriks
                    print(f"Posisi tidak valid. Masukkan kembali!")
                    a = int(input("Lokasi mendatar pilihan: "))
                    b = int(input("Lokasi vertikal pilihan: "))
                elif ttt[a-1][b-1] != "-": # Lokasi yang diinginkan sudah diduduki oleh suatu elemen yang bukan "-"
                    print(f"Posisi tersebut sudah ditempati oleh {ttt[a-1][b-1]}. Masukkan kembali!")
                    a = int(input("Lokasi mendatar pilihan: "))
                    b = int(input("Lokasi vertikal pilihan: "))
            if 1 <= a <= 3 and 1 <= b <= 3 and ttt[a-1][b-1] == "-":
                ttt[a-1][b-1] = "X"
         
        else: # Apabila i genap, giliran jatuh ke pemain 2   
            print(f"Giliran {int((i + 1) / 2)} Pemain O:")
            c = int(input("Lokasi mendatar pilihan: "))
            d = int(input("Lokasi vertikal pilihan: "))
            while True:
                if 1 <= c <= 3 and 1 <= d <= 3 and ttt[c-1][d-1] == "-":
                    break
                elif c < 1 or c > 3 or d < 1 or d > 3: # Masukan posisi tictactoe diluar jangkauan matriks
                    print(f"Posisi tidak valid. Masukkan kembali!")
                    c = int(input("Lokasi mendatar pilihan: "))
                    d = int(input("Lokasi vertikal pilihan: "))
                elif ttt[c-1][d-1] != "-": # Lokasi yang diinginkan sudah diduduki oleh suatu elemen yang bukan "-"
                    print(f"Posisi tersebut sudah ditempati oleh {ttt[c-1][d-1]}. Masukkan kembali!")
                    c = int(input("Lokasi mendatar pilihan: "))
                    d = int(input("Lokasi vertikal pilihan: "))
            if 1 <= c <= 3 and 1 <= d <= 3 and ttt[c-1][d-1] == "-":
                ttt[c-1][d-1] = "O"
        
        # Matriks ttt ditampilkan lagi dengan elemen yang sudah dimasukkan pemain
        print("\n")
        for l in range(3):
            for k in range(3):
                print(ttt[l][k], end = " ")
            print()
        print("\n")

        # Ada kemungkinan program dihentikan apabila ditemukan pemenang sebelum mencapai 9 giliran
        if i < 8:
            for k in range(3):
                # Kemenangan diperoleh pemain dengan elemen yang sama pada sebuah baris
                if ttt[k][0] ==  ttt[k][1] and ttt[k][1] ==  ttt[k][2] and ttt[k][0] != "-":
                    Win = ttt[k][0]
                    isWin = True
                for l in range(3): # Kemenangan diperoleh pemain dengan elemen yang sama pada sebuah kolom
                    if ttt[0][l] ==  ttt[1][l]  and ttt[1][l] == ttt[2][l] and ttt[0][l] != "-":
                        Win = ttt[0][l]
                        isWin = True
            # Kemenangan diperoleh pemain dengan elemen yang sama secara diagonal
            if ttt[0][0] == ttt[1][1] and ttt[1][1] ==  ttt[2][2] and ttt[0][0] != "-":
                Win = ttt[1][1]
                isWin = True
            elif ttt[0][2] == ttt[1][1] and ttt[1][1] == ttt[2][0] and ttt[2][0] != "-":
                Win = ttt[1][1]
                isWin = True

        # Jika ditemukan pemenang, permainan dihentikan, dan pemenang diumumkan
        if isWin:
            print(f"Pemain {Win} menang. Selamat!")
            break
        elif i == 8 and (not isWin): # Jika tidak ada pemenang setelah 9 giliran berlalu
            print("Game seri.")

# Pemanggilan fungsi
tictactoe()
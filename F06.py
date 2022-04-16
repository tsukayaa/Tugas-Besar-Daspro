from helpbase import *

def ubah_stok() :
    global game_data
    ID = input("Masukan ID: ")
    id_ada = search_id(ID)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False :
        print("Tidak ada game dengan ID tersebut!")
        return
    else : # Untuk kasus bahwa ID ada
        urutanID = search_id(ID)[1]
        stok_awal = game_data[urutanID][5] #[5] adalah letak dari kolom 'stok'
        jumlah = int(input("Masukan Jumlah: "))
        if int(stok_awal) + jumlah < 0 : # Apabila stoknya menjadi negatif karena kebuang terlalu banyak
            print('Stok Game', game_data[urutanID][1], 'Gagal dibuang karena stok kurang. Stok sekarang:', stok_awal, "(<", str(jumlah*-1) + ")")
        else : #Untuk kasus stoknya tetap valid
            game_data[urutanID][5] = str(int(stok_awal) + jumlah)
            if(jumlah > 0):
                print("Stok Game", game_data[urutanID][1], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal) + jumlah))
            else:
                print("Stok Game", game_data[urutanID][1], "berhasil dikurangi. Stok sekarang:",str(int(stok_awal) + jumlah))

ubah_stok()

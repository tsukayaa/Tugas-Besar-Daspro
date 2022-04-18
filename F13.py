from helpbase import *

def riwayat(userid) :
    cek = False
    for i in range (length(riwayat_data)) :
        if userid == riwayat_data[i][3] :
            cek = True
            print("Daftar game: ")
            print(riwayat_data[i][0], " | ", riwayat_data[i][1], " | ", riwayat_data[i][2], " | ", riwayat_data[i][4])
    if cek == False :
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")

# riwayat("0")
# riwayat("1")
# riwayat("3")

from helpbase import *

def search_game_at_store () :
    id_game = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga_game = input("Masukkan Harga Game: ")
    kategori_game = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    
    arr = filtergame(filtergame(filtergame(filtergame(filtergame(game_data,tahun_rilis,3),kategori_game,2),harga_game,4),nama_game,1),id_game,0)
    print("Daftar game pada toko yang memenuhi kriteria: ")
    for i in range (length(arr)) :
        print(arr[i][0], " | ", arr[i][1], " | ", arr[i][4], " | ", arr[i][2], " | ", arr[i][3], " | ", arr[i][5])

search_game_at_store()

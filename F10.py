from helpbase import *

def search_my_game(userid):
    idgame = str(input("Masukkan ID Game: "))
    tahun_rilis = str(input("Masukkan Tahun Rilis Game:"))
    cek = False
    print("Daftar game pada inventory yang memenuhi kriteria: ")
    for i in range(length(kepemilikan_data)) :
        if idgame == game_data[i][0] and tahun_rilis == game_data[i][3] :
            cek = True
            filterkepemilikan(filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0),userid)   
    if cek == False :
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

search_my_game("2")

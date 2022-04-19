from helpbase import *

def search_my_game(userid):
    idgame = str(input("Masukkan ID Game: "))
    tahun_rilis = str(input("Masukkan Tahun Rilis Game:"))

    print("Daftar game pada inventory yang memenuhi kriteria: ")
    arr = filterkepemilikan(filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0),userid)   
    if arr == [] :
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        
search_my_game("2")

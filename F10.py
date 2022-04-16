from helpbase import *

def search_my_game(userid):
    idgame = str(input("Masukkan ID Game: "))
    tahun_rilis = str(input("Masukkan Tahun Rilis Game:"))
    
    filterkepemilikan(filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0),userid)

# search_my_game("2")

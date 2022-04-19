from helpbase import *

def search_my_game(userid):
    idgame = str(input("Masukkan ID Game: "))
    tahun_rilis = str(input("Masukkan Tahun Rilis Game:"))
    print("Daftar game pada inventory yang memenuhi kriteria: ")

    file = filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0)
    arr = []

    for i in range(length(file)):
        for j in range(length(kepemilikan_data)):
            if (file[i][0] == kepemilikan_data[j][0] and str(userid) == kepemilikan_data[j][1]) :
                arr += file[i]
                print(kepemilikan_data[j][0], " | ", file[i][1], " | ", file[i][4], " | ", file[i][2], " | ", file[i][3])
    
    if arr == [] :
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

search_my_game("2")

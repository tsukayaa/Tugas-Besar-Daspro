from helpbase import *

def buy_game(users_id):
    global game_data
    global kepemilikan_data
    game_id = input("Masukkan ID game :")
    temp = search_id(game_id)
    if(not temp[0]):
        print("Tidak ada game dengan ID tersebut")
        return
    else:
        for i in range(length(kepemilikan_data)):  # case users sudah memiliki gamenya
            if (users_id == int(kepemilikan_data[i][1]) and game_id == kepemilikan_data[i][0]):
                print("Anda sudah memiliki Game tersebut!")
                return
        nama_game = str
        stok_game = int  # var menyimpan stok game
        harga_game = int  # var menyimpan harga dari gamenya
        for i in range(length(game_data)):
            if (game_id == game_data[i][0]):
                harga_game = int(game_data[i][4])
                stok_game = int(game_data[i][5])
                nama_game = game_data[i][1]

        saldo_user = int  # var menyimpan banyak saldo users
        for i in range(length(user_data)):
            if (users_id == int(user_data[i][0])):
                saldo_user = int(user_data[i][5])
        print(saldo_user,stok_game,harga_game)
        if(saldo_user < harga_game) :
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            return
        if(stok_game < 0):
            print("Stok Game tersebut sedang habis!")
            return
        game_data[temp[1]][5] = str(int(game_data[temp[1]][5]) - 1)
        # with open('data/game.csv','r') as file:         #tulis ulang game.csv
        #     head = file.readline()
        # line = []
        # for i in range (length(game_data)):
        #     line += change_to_csv('data/game.csv',game_data[i])
        # with open('data/game.csv','w') as file:
        #     file.write(head)
        #     for i in range(length(line)):
        #         file.write(line[i])               #batas bagian tulis ulang game.csv
        # with open('data/kepemilikan.csv', 'r') as file:   #tulis ulang kepemilikan.csv
        #     head = file.readline()
        # line = []
        # for i in range(length(kepemilikan_data)):
        #     line += [change_to_csvkepemilikan('data/kepemilikan.csv', kepemilikan_data[i])]
        # #print(line)
        # lastline = game_id + ';' + str(users_id) # ini adalah data kepemilikan users_id terhadap nama_game
        # with open('data/kepemilikan.csv', 'w') as file:
        #     file.write(head)
        #     for i in range(length(line)):
        #         file.write(line[i])
        #     file.write(lastline)                    #batas bagian tulis ulang kepemilikan.csv
        print("Game", nama_game," berhasil dibeli!")

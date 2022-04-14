from helpbase import *

def list_game(users_id):
    punyagame = False
    daftar_game = [] #list game yang dimiliki user
    for i in range(length(kepemilikan_data)):
        if(users_id == int(kepemilikan_data[i]['user_id'])):
            punyagame = True
            daftar_game += [kepemilikan_data[i]['game_id']]
    if(not punyagame):
        print("Maaf, kamu belum membeli game. Ketik perintah",'\033[1m' + 'beli_game' + '\033[0m',"untuk beli.")
    else:
        for i in range(length(daftar_game)):
            for j in range(length(game_data)):
                if(daftar_game[i] == game_data[j]['id']):
                    print(game_data[j]['id'], " | ", game_data[j]['nama'], " | ", game_data[j]['kategori']," | ", game_data[j]['tahun_rilis'], " | ", game_data[j]['harga'], " | ",game_data[j]['stok'])


list_game(1)

from helpbase import *

def sorting(keyword):
    temp = []

    if(keyword == 'tahun+'): #jika keyword adalah tahun+
        for i in range(length(game_data)):
            temp += [[game_data[i]['tahun_rilis'],i]]
            #temp[i][0] berisi tahun rilis, sementara temp[i][1] berisi urutan baris dari game_datanya
        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] > temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp
    elif (keyword == 'tahun-'): #jika keyword adalah tahun-
        for i in range(length(game_data)):
            temp += [[game_data[i]['tahun_rilis'],i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] < temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    elif (keyword == 'harga+'):
        for i in range(length(game_data)):
            temp += [[game_data[i]['harga'],i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] > temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    elif (keyword == 'harga-'):
        for i in range(length(game_data)):
            temp += [[game_data[i]['harga'],i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] < temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    else:
        for i in range(length(game_data)):
            temp += [[game_data[i]['id'],i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] > temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp


def list_game_toko():
    keyword = input("Skema sorting:")
    if(keyword == '' or keyword == 'tahun+' or keyword == 'harga-' or keyword == 'harga+' or keyword == 'tahun-'):
        temp = sorting(keyword)
        for i in range (length(game_data)):
            print(game_data[temp[i][1]]['id']," | ",game_data[temp[i][1]]['nama']," | ",game_data[temp[i][1]]['kategori']," | ",game_data[temp[i][1]]['tahun_rilis']," | ",game_data[temp[i][1]]['harga']," | ",game_data[temp[i][1]]['stok'])
            #print(game_data[temp[i][1]]['id']," | ", game_data[temp[i][1]]['nama'], "\t | ", game_data[temp[i][1]]['kategori'], "\t | ",game_data[temp[i][1]]['tahun_rilis'], " | ", game_data[temp[i][1]]['harga'], " | ", game_data[temp[i][1]]['stok'])
    else:
        print("Skema sorting tidak valid!")

list_game_toko()


from helpbase import *

def filtergame(file,keyword,key):

    if keyword == '':
        return file
    else:
        arr = []
        for i in range(length(file)):
            # print(file[i][key])
            if(file[i][key] == keyword):
                arr += [file[i]]
        # print(arr)
        return arr

# filtergame(filtergame(game_data,'2022',3),'Dasar Pemrograman',1)

def filterkepemilikan(file,id):
    id = str(id)
    arr = []
    for i in range(length(file)):
        for j in range(length(kepemilikan_data)):
            #print(file[i][0],kepemilikan_data[j][0],kepemilikan_data[j][1],id)
            if (file[i][0] == kepemilikan_data[j][0] and id == kepemilikan_data[j][1]):
               # print('a')
                arr += file[i]
                print(kepemilikan_data[j][0], " | ", file[i][1], " | ", file[i][4], " | ", file[i][2], " | ", file[i][3])
    # print(arr)
    return arr

# filterkepemilikan(filtergame(game_data,'2022',3),1)

def search_my_game(userid):
    idgame = str(input("id: "))
    tahun_rilis = str(input("tahun:"))
    filterkepemilikan(filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0),userid)
    
search_my_game("2")
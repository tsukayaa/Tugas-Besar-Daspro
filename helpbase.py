import argparse
import sys
import os

def load(): #F15
    parser = argparse.ArgumentParser()

    parser.add_argument("nama_folder")
    args=parser.parse_args()

    input_path = args.nama_folder

    if not os.path.isdir(input_path):
        print('Folder ' + input_path +' tidak ditemukan')
        sys.exit()
    else:
        print('Selamat datang di antarmuka Binomo')
        kepemilikan_data = change_to_array(input_path + '/'+'kepemilikan.csv')
        game_data = change_to_array(input_path + '/'+'game.csv')
        user_data = change_to_array(input_path + '/'+'user.csv')
        riwayat_data = change_to_array(input_path + '/'+'riwayat.csv')
        #change_to_array(input_path+'game.csv')
        #change_to_array(input_path+'user.csv')
        #change_to_array(input_path+'riwayat.csv')
        #change_to_array(input_path+'kepemilikan.csv')
        return kepemilikan_data,game_data,user_data,riwayat_data,input_path

def length(filename): #Fungsi len dengan implementasi sendiri
    count = 0
    for i in filename:
        count += 1
    return count

def search_id(ID,game_data) :
    id_ada = False # Untuk mengecek apakah ID sudah ada atau tidak
    urutan_id = -1
    for i in range (length(game_data)) : # Mengecek apakah id ada di data gadget
        if ID == game_data[i][0] : #[0] merupakan kolom dari 'id'
            id_ada = True
            urutan_id = i
            break
    return id_ada, urutan_id


def change_to_csv(query): #ini digunakan untuk mengubah array temp menjadi csv
    string = ''

    for i in range(length(query)):
        if(i == length(query) - 1):
            string += query[i]
        else:
            string += query[i]
            string += ';'

    string += '\n'

    return string


def split_csv(string, delimiters=";\n"):
    result = []
    word = ""
    for i in string:
        if i not in delimiters:
            word += i
        elif word:
            result += [[word]]
            word = ""
    if word:
        result += [[word]]
    return result

def get_header(filename):
    with open(filename, 'r',encoding='utf-8') as file_data:
        head_data = file_data.readlines()[0]
        head_data = split_csv(head_data)

        head_data = remove_if_last_enter(head_data)
        return head_data

def remove_if_last_enter(arr):
    result = []
    temp = ""
    last_member = arr[length(arr) - 1]
    if last_member[length(last_member) - 1] == '\n':
        for i in range(length(last_member) - 1):
            temp += (last_member[i])
    result += [[temp]]
    return result
# def remove_if_last_enter(arr):
#     last_member = arr[length(arr) - 1]
#     if last_member[length(last_member) - 1] == '\n':
#         arr[length(arr) - 1] = last_member[:len(last_member) - 1]
#
#     return arr

def get_all_data(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        read_line = f.readlines()
    arr = []
    for line in read_line:
        arr += remove_if_last_enter([line])
    temp = []
    for i in range(length(arr)):
        if i >= 1:
            temp += [arr[i]]
    return temp

###################
def change_to_array(filename):
    arr = get_all_data(filename)
    clean = []

    for data in arr:
        clean += [split_csv(data)]
    return clean

def slicing (arr,n,m): #arr[1:]
    arr_baru = []
    for i in range (n, m):
        arr_baru += arr[i]
    return arr_baru

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

def filterkepemilikan(file,id,kepemilikan_data):
    id = str(id)
    arr = []
    for i in range(length(file)):
        for j in range(length(kepemilikan_data)):
            #print(file[i][0],kepemilikan_data[j][0],kepemilikan_data[j][1],id)
            if (file[i][0] == kepemilikan_data[j][0] and id == kepemilikan_data[j][1]):
               # print('a')
                arr += [file[i]]
                #print(kepemilikan_data[j][0], " | ", file[i][1], " | ", file[i][4], " | ", file[i][2], " | ", file[i][3])
    # print(arr)
    return arr



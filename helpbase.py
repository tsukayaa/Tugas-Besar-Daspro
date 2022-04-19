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


def length(filename): #Fungsi len dengan implementasi sendiri
    count = 0
    for i in filename:
        count += 1
    return count

def search_id(ID) :
    id_ada = False # Untuk mengecek apakah ID sudah ada atau tidak
    urutan_id = -1
    for i in range (length(game_data)) : # Mengecek apakah id ada di data gadget
        if ID == game_data[i][0] : #[0] merupakan kolom dari 'id'
            id_ada = True
            urutan_id = i
            break
    return id_ada, urutan_id

# def sort_by_key(arr, key):
#     newlist = sorted(arr, key=lambda k: int(k[key]))
#     return newlist
#
# def get_last_id(filename):
#     arr = get_all_to_dictionary(filename)
#
#     after_sorted = sort_by_key(arr, 'id')
#     last_element = after_sorted[-1]
#
#     return int(last_element['id'])

def change_to_csv(filename, query): #ini digunakan untuk mengubah array temp menjadi csv
    head = get_header(filename)
    string = ''
  # #  x = query.get('id'
  #  # print(x)
  #  # if query.get('id') == None:
  # #      query['id'] = get_last_id(filename) + 1
  #   if(filename == 'data/game.csv' or filename == 'data/user.csv'):
  #       #string += query['id']
  #       string += query[0]
  #   else:
  #       string += query[0]

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
            result.append(word)
            word = ""
    if word:
        result.append(word)
    return result



def get_header(filename):
    with open(filename, 'r',encoding='utf-8') as file_data:
        head_data = file_data.readlines()[0]
        head_data = split_csv(head_data)

        head_data = remove_if_last_enter(head_data)
        return head_data

def remove_if_last_enter(arr):
    last_member = arr[len(arr) - 1]
    if last_member[len(last_member) - 1] == '\n':
        arr[len(arr) - 1] = last_member[:len(last_member) - 1]

    return arr
    #######################

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
   # print(temp)
    return temp

###################
def change_to_array(filename):
    arr = get_all_data(filename)

    head = get_header(filename)
    clean = []
    return_data = []

    for data in arr:
        clean += [split_csv(data)]
   #  print(clean)
   # # print(head)
   #  for i in clean:
   #      temp = {}
   #
   #      for j in range(length(head)):
   #          temp[head[j]] = i[j]
   #     # print(temp)
   #      return_data += [temp]
   # # print(return_data)
    return clean

def rewrite(filename):
    print('data/' + filename)
    global game_data,users_data,kepemilikan_data
    if(filename == 'game.csv'):
        temp = game_data
    elif(filename == 'user.csv'):
        temp = user_data
    elif(filename == 'kepemilikan.csv'):
        temp = kepemilikan_data
   # print(temp)
    with open('data/' + filename, 'r') as file:
        head = file.readlines()[0]
    lines = []
    for i in range(length(temp)):
        lines += [change_to_csv('data/' + filename,temp[i])]
   # print(lines)
    with open('data/' + filename, 'w') as file:
        file.write(head)
        for i in range(length(temp)):
            file.write(lines[i])
    #print(head)

# def rewrite(filename)
#     global game_data,kepemilikan_data,users_data,riwayat_data
#     with open('data/' + filename, 'r') :
def slicing (arr,n,m): #arr[1:]
    arr_baru = []
    for i in range (n, m):
        arr_baru += arr[i]
    return arr_baru

kepemilikan_data = change_to_array('data/kepemilikan.csv')
game_data = change_to_array('data/game.csv')
user_data = change_to_array('data/user.csv')
aksesadmin = False #untuk menandakan apakah role user sekarang adalah admin/user
idcurrentuser = None #id dari user yang login sekarang, digunakan sebagai parameter
                    #dari fungsi yang memerlukan id user
#riwayat_data = change_to_dictionary('data/riwayat.csv')

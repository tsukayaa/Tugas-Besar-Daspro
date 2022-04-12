def dict_to_csv(filename, query):
    head = get_header(filename)
    string = ''

    if query.get('id') == None:
        query['id'] = get_last_id(filename) + 1

    string += query['id']

    for head_data in head[1:]:
        string += ';' + query[head_data]

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

def remove_if_last_enter(arr):
    last_member = arr[len(arr)-1]
    if last_member[len(last_member)-1] == '\n':
        arr[len(arr)-1] = last_member[:len(last_member)-1]

    return arr

def get_header(filename):
    with open(filename, 'r') as file_data:
        head_data = file_data.readlines()[0]
        head_data = split_csv(head_data)

        head_data = remove_if_last_enter(head_data)
        return head_data

    #######################

def get_all_data(filename):
    with open(filename, 'r') as f:
        read_line = f.readlines()

    arr = []
    for line in read_line:
        arr.append(''.join(remove_if_last_enter(list(line))))

    return arr[1:]

###################
def get_all_to_dictionary(filename):
    arr = get_all_data(filename)

    head = get_header(filename)
    clean = []
    return_data = []

    for data in arr:
        clean.append(split_csv(data))

    for i in clean:
        temp = {}

        for j in range(len(head)):
            temp[head[j]] = i[j]

        return_data.append(temp)

    return return_data

#####################
def mencari_id(ID) :
    id_ada = False # Untuk mengecek apakah ID sudah ada atau tidak
    urutan_id = -1
    datagadget = get_all_to_dictionary('data/game.csv')
    for i in range (len(datagadget)) : # Mengecek apakah id ada di data gadget
        if ID == datagadget[i]['id'] :
            id_ada = True
            urutan_id = i
            break
    return id_ada, urutan_id

def ubah_stok() :
    ID = input("Masukan ID: ")
    id_ada = mencari_id(ID)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False :
        print("Tidak ada game dengan ID tersebut!")
        return
    else : # Untuk kasus bahwa ID ada
        urutanID = mencari_id(ID)[1]
        data = get_all_to_dictionary('data/game.csv')
        stok_awal = data[urutanID]['stok']
        jumlah = int(input("Masukan Jumlah: "))
        if int(stok_awal) + jumlah < 0 : # Apabila stoknya menjadi negatif karena kebuang terlalu banyak
            print(jumlah, data[urutanID]['nama'], 'Gagal dibuang karena stok kurang. Stok sekarang:', stok_awal, "(<", str(jumlah*-1) + ")")
        else : #Untuk kasus stoknya tetap valid
            data[urutanID]['stok'] = str(int(stok_awal) + jumlah)
            with open('data/game.csv', 'r') as user_file:
                head = user_file.readline()
            lines = []
            for i in range (len(data)) :
                lines += [dict_to_csv('data/game.csv',data[i])]
            with open('data/game.csv', 'w') as user_file: #Untuk menuliskan data yang baru ke CSV gadget
                user_file.write(head)
                for i in range (len(data)) :
                    user_file.write(lines[i])
                    user_file.write(lines[i])
            print(jumlah, data[urutanID]['nama'], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal)+jumlah))

ubah_stok()
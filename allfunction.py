

#File ini berisi seluruh fungsi daripada F4 - F14 dan F16

# Deskripsi : Menambah game ke toko game
# Penambahan game pada toko game dilakukan melalui pengisian informasi game yang akan ditambahkan.
# Program lalu akan melakukan validasi apakah semua informasi yang dibutuhkan telah diinput oleh admin.
# Apabila terdapat informasi yang belum dimasukkan oleh pengguna, program akan meminta input lagi kepada pengguna.
# Hal ini akan dilakukan terus menerus sampai pengguna telah melakukan input semua informasi game.
# Game baru yang telah ditambahkan akan disimpan pada file csv.

# akses : admin
# berfungsi untuk mengambil data dari game.csv
# menambah game yang diinput ke csv --> ada di fungsional save
# pada fungsi ini, penambahan game dimasukkan ke memori bukan ke csv

# >>> tambah_game
from helpbase import *
import os
import datetime

def tambah_game(game_data): #F04
    for i in range(length(game_data)):
        if i == length(game_data) - 1 :
            latestid = game_data[i][0]
    latestid = slicing(latestid,4,7)
    id_game = int(latestid[0]) * 100 + int(latestid[1]) * 10 + int(latestid[2]) * 1
    id_game += 1
    id_game = str(id_game)
    if(length(id_game) == 1):
        id_game = '00' + id_game
    elif(length(id_game) == 2):
        id_game = '0' + id_game
    id_game = 'GAME' + id_game

    nama_game = ''
    kategori_game = ''
    tahun_rilis = ''
    harga_game = ''
    stok_awal = ''
    while (nama_game=='') or (kategori_game=='') or (tahun_rilis=='') or (harga_game=='') or (stok_awal==''):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO")
        nama_game = str(input("Masukkan nama game: "))
        kategori_game = str(input("Masukkan kategori: "))
        tahun_rilis = str(input("Masukkan tahun rilis: "))
        harga_game = str(input("Masukkan harga: "))
        stok_awal = str(input("Masukkan stok awal: "))
    print('Selamat! Berhasil menambahkan game', nama_game)
    game_baru = [id_game,nama_game, kategori_game, tahun_rilis, harga_game, stok_awal]
    game_data += [game_baru]
    return game_data

# nama_game = input("Masukkan nama game: ")
# kategori_game = input("Masukkan kategori: ")
# tahun_rilis = input("Masukkan tahun rilis: ")
# harga_game = input("Masukkan harga: ")
# stok_awal = input("Masukkan stok awal: ")
# tambah_game(nama_game,kategori_game,tahun_rilis,harga_game,stok_awal)

def ubah_game(game_data): #F05
    id_game = input("Masukkan ID Game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    for row in range (length(game_data)):
        #print(game_data[row][0],id_game)
        if game_data[row][0] == id_game:
            print('a')
            if (nama_game != ''):
                game_data[row][1] = nama_game
            if (kategori != ''):
                game_data[row][2] = kategori
            if (tahun_rilis != ''):
                game_data[row][3] = tahun_rilis
            if (harga != ''):
                game_data[row][4] = harga
    #print(game_data)
    return game_data

def ubah_stok(game_data) : #F06
    ID = input("Masukan ID: ")
    id_ada = search_id(ID,game_data)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False :
        print("Tidak ada game dengan ID tersebut!")
        return
    else : # Untuk kasus bahwa ID ada
        urutanID = search_id(ID,game_data)[1]
        stok_awal = game_data[urutanID][5] #[5] adalah letak dari kolom 'stok'
        jumlah = int(input("Masukan Jumlah: "))
        if int(stok_awal) + jumlah < 0 : # Apabila stoknya menjadi negatif karena kebuang terlalu banyak
            print('Stok Game', game_data[urutanID][1], 'Gagal dibuang karena stok kurang. Stok sekarang:', stok_awal, "(<", str(jumlah*-1) + ")")
        else : #Untuk kasus stoknya tetap valid
            game_data[urutanID][5] = str(int(stok_awal) + jumlah)
            if(jumlah > 0):
                print("Stok Game", game_data[urutanID][1], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal) + jumlah))
            else:
                print("Stok Game", game_data[urutanID][1], "berhasil dikurangi. Stok sekarang:",str(int(stok_awal) + jumlah))

def sorting(keyword,game_data):
    temp=[]
    if(keyword == 'tahun+'): #jika keyword adalah tahun+
        for i in range(length(game_data)):
            temp += [[int(game_data[i][3]),i]]
            #print(temp)
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
            temp += [[int(game_data[i][3]),i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] < temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    elif (keyword == 'harga+'):
        for i in range(length(game_data)):
            temp += [[int(game_data[i][4]),i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] > temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    elif (keyword == 'harga-'):
        for i in range(length(game_data)):
            temp += [[int(game_data[i][4]),i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] < temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp

    else:
        for i in range(length(game_data)):
            latestid = game_data[i][0]
            latestid = slicing(latestid, 4, 7)
            id_game = int(latestid[0]) * 100 + int(latestid[1]) * 10 + int(latestid[2]) * 1
            temp += [[id_game,i]]

        for i in range(length(temp)):
            for j in range(i + 1, length(temp)):
                if (temp[i][0] > temp[j][0]):
                    x = temp[i]
                    temp[i] = temp[j]
                    temp[j] = x

        return temp


def list_game_toko(game_data):  #F07
    keyword = input("Skema sorting:")
    if(keyword == '' or keyword == 'tahun+' or keyword == 'harga-' or keyword == 'harga+' or keyword == 'tahun-'):
        temp = sorting(keyword,game_data)
        for i in range (length(game_data)):
            print(game_data[temp[i][1]][0]," | ",game_data[temp[i][1]][1]," | ",game_data[temp[i][1]][2]," | ",game_data[temp[i][1]][3]," | ",game_data[temp[i][1]][4]," | ",game_data[temp[i][1]][5])
            #print(game_data[temp[i][1]]['id']," | ", game_data[temp[i][1]]['nama'], "\t | ", game_data[temp[i][1]]['kategori'], "\t | ",game_data[temp[i][1]]['tahun_rilis'], " | ", game_data[temp[i][1]]['harga'], " | ", game_data[temp[i][1]]['stok'])
    else:
        print("Skema sorting tidak valid!")

def buy_game(users_id,kepemilikan_data,game_data,user_data,riwayat_data): #F08
    game_id = input("Masukkan ID game :")
    temp = search_id(game_id,game_data)
    if(not temp[0]):
        print("Tidak ada game dengan ID tersebut")
        return
    else:
        for i in range(length(kepemilikan_data)):  # case users sudah memiliki gamenya
            if (users_id == int(kepemilikan_data[i][1]) and game_id == kepemilikan_data[i][0]):
                print("Anda sudah memiliki Game tersebut!")
                return kepemilikan_data,game_data,user_data,riwayat_data
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
            return kepemilikan_data,game_data,user_data,riwayat_data
        if(stok_game < 0):
            print("Stok Game tersebut sedang habis!")
            return kepemilikan_data,game_data,user_data,riwayat_data
        tanggal_beli = datetime.datetime.now()
        tahun_beli = tanggal_beli.year
        game_data[temp[1]][5] = str(int(game_data[temp[1]][5]) - 1)
        kepemilikan_data += [[game_id,str(users_id)]]
        riwayat_data += [[game_id,nama_game,str(harga_game),str(users_id),str(tahun_beli)]]
        print("Game", nama_game," berhasil dibeli!")
        return kepemilikan_data,game_data,user_data,riwayat_data

def list_game(users_id,kepemilikan_data,game_data): #F09
    punyagame = False
    daftar_game = [] #list game yang dimiliki user
    for i in range(length(kepemilikan_data)):
        if(users_id == int(kepemilikan_data[i][1])):
            punyagame = True
            daftar_game += [kepemilikan_data[i][0]]
    if(not punyagame):
        print("Maaf, kamu belum membeli game. Ketik perintah",'\033[1m' + 'beli_game' + '\033[0m',"untuk beli.")
    else:
        for i in range(length(daftar_game)):
            for j in range(length(game_data)):
                if(daftar_game[i] == game_data[j][0]):
                    print(game_data[j][0], " | ", game_data[j][1], " | ", game_data[j][2]," | ", game_data[j][3], " | ", game_data[j][4], " | ",game_data[j][5])

def search_my_game(userid,kepemilikan_data,game_data): #F10
    userid = str(userid)
    idgame = str(input("Masukkan ID Game: "))
    tahun_rilis = str(input("Masukkan Tahun Rilis Game:"))
    file = filterkepemilikan(filtergame(filtergame(game_data,tahun_rilis,3),idgame, 0),userid,kepemilikan_data)
    #print(file)
    if length(file) == 0 :
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        print("Daftar game pada inventory yang memenuhi kriteria: ")
        for i in range (length(file)):
            print(file[i][0], " | ", file[i][1], " | ", file[i][4], " | ", file[i][2], " | ", file[i][3])


def search_game_at_store(game_data): #F11
    id_game = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga_game = input("Masukkan Harga Game: ")
    kategori_game = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    arr = filtergame(
        filtergame(filtergame(filtergame(filtergame(game_data, tahun_rilis, 3), kategori_game, 2), harga_game, 4),
                   nama_game, 1), id_game, 0)
    if length(arr) == 0:
        print("Tidak ada game yang memenuhi kriteria")
    else:
        print("Daftar game pada toko yang memenuhi kriteria: ")
        for i in range(length(arr)):
            print(arr[i][0], " | ", arr[i][1], " | ", arr[i][4], " | ", arr[i][2], " | ", arr[i][3], " | ", arr[i][5])

def topup(user_data): #F12
    username = input("Masukan username: ")
    saldo = input("Masukan saldo: ")
    isunamevalid = False

    for i in range(0, length(user_data)):
        if username == user_data[i][1]:
            isunamevalid = True
            nama = user_data[i][2]
            balance = int(user_data[i][5])
            urutanID = i

    if (not isunamevalid):
        print(f"Username {username} tidak ditemukan.")
    else:
        if (int(user_data[urutanID][5]) + int(saldo)) < 0:
            print("Masukan tidak valid.")
        else:
            newbalance = int(saldo) + balance
            user_data[urutanID][5] = str(newbalance)
            if (int(saldo) > 0):
                print(f"Top up berhasil. Saldo {nama} bertambah menjadi {newbalance}.")
            else:
                print(f"Top up berhasil. Saldo {nama} berkurang menjadi {newbalance}.")
    return user_data

def riwayat(userid,riwayat_data) : #F13
    userid = str(userid)
    cek = False
    for i in range (length(riwayat_data)) :
        if userid == riwayat_data[i][3] :
            cek = True
    if cek == False :
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else :
        print("Daftar game: ")
        for i in range(length(riwayat_data)):
            if userid == riwayat_data[i][3]:
                print(riwayat_data[i][0], " | ", riwayat_data[i][1], " | ", riwayat_data[i][2], " | ", riwayat_data[i][4])

def help(aksesadmin): #F14
    if(aksesadmin):
        print(""" ============ HELP ============
            1. register - Untuk melakukan registrasi user baru
            2. tambah_game - Untuk menambah game yang dijual pada toko
            3. ubah_game - Untuk mengubah game pada toko game
            4. ubah_stok - Untuk mengubah stok game pada toko
            5. list_game_toko - Untuk melihat game yang ada pada toko
            6. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
            7. topup - Untuk menambahkan saldo kepada user
            8. help - Untuk melihat panduan penggunaan
            9. save - Untuk menyimpan perubahan
            10. exit - Untuk keluar
             """)
    # user atau belum login
    else:
        print(""" ============ HELP ============
            1. list_game_toko - Untuk melihat game yang ada pada toko
            2. buy_game - Untuk membeli game
            3. list_game - Untuk menampilkan daftar game yang dimiliki
            4. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis
            5. search_game_at_store - Untuk mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis
            6. riwayat - Untuk melihat riwayat pembelian game
            7. help - Untuk melihat panduan penggunaan
            8. save - Untuk menyimpan perubahan
            9. exit - Untuk keluar
            """)




# Algoritma
# >>> save
def save(kepemilikan_data,game_data,user_data,riwayat_data ,nama_folder):
    folder_tujuan = input("Masukkan nama folder penyimpanan: ")
    print("Saving...")

    belum_ada = 1
    if not os.path.isdir(folder_tujuan):
        os.system('mkdir ' + folder_tujuan)
        belum_ada = 0

    # copy data

    header = [
        'game_id;user_id',
        'id;nama;kategori;tahun_rilis;harga;stok',
        'id;username;nama;password;role;saldo',
        'game_id;nama;harga;user_id;tahun_beli',
    ]

    writingfile(kepemilikan_data, nama_folder, folder_tujuan, 'kepemilikan.csv', belum_ada, header[0])
    writingfile(game_data, nama_folder, folder_tujuan, 'game.csv', belum_ada, header[1])
    writingfile(user_data, nama_folder, folder_tujuan, 'user.csv', belum_ada, header[2])
    writingfile(riwayat_data, nama_folder, folder_tujuan, 'riwayat.csv', belum_ada, header[3])

    print("Data telah disimpan pada folder " + folder_tujuan + '!')


def writingfile(data, from_folder, to_folder, csv_name, belum_ada, header):
    os.chdir(to_folder)
    if os.name == 'nt':
        os.system("cd . > " + csv_name)
    else:
        os.system("touch " + csv_name)

    os.chdir('..')
    string = ''
    with open(to_folder + '/' + csv_name, 'w',encoding='utf-8') as f:
        head = split_csv(header)
        for i in range(length(head)):
            if i == length(head) - 1:
                string += head[i]
            else:
                string += head[i] + ';'
    string += '\n'
    lines = []
    for i in range(length(data)):
        lines += [change_to_csv(data[i])]
    # print(lines)
    with open(to_folder + '/' + csv_name, 'w', encoding='utf-8') as file:
        file.write(string)
        for i in range(length(data)):
            file.write(lines[i])

    # with open(to_folder + '/' + csv_name, 'w') as f:
    #     head = split_csv(header)
    #     string = ''
    #     for i in head:
    #         string += i + ';'
    #
    #     string = string[:len(string) - 1]
    #     f.writelines(string)
    # for i in data:
    #     create(i, to_folder + '/' + csv_name)

